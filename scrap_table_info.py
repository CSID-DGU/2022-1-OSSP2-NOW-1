from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from css_parser import css_parser
from lecture import Lecture

# 크롬 드라이버 자동으로 설치해주는 매니저

# id = input("아이디 입력 : ")
# password = input("비밀번호 입력 :")


class loginError(Exception):
    """
    로그인에 실패할 때 발생하는 에러
    """

    def __init__(self):
        super().__init__('로그인에 실패했습니다')


class NoBrowserError(Exception):
    """
    크롬 브라우저가 설치되지 않은 경우 발생하는 에러
    """

    def __init__(self):
        super().__init__('크롬 브라우저가 설치되어 있지 않습니다. 설치해주세요')


def user_login(id: str, password: str):
    #크롬 설치 여부 검사#
    browser : WebDriver
    try:
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
    except Exception as e:
        # 크롬 브라우저가 없는 상황. 크롬 브라우저를 설치해달라는 메시지 전달.
        print("최신 크롬 브라우저를 설치해주세요!")
        return

    ############################################################################
    #사이트 지정 및 화면 사이즈 지정#
    browser.set_window_size(1920, 1680)  # 화면 사이즈 지정

    browser.get("https://www.everytime.kr/login")  # 에브리타임 로그인 사이트 접근

    ############################################################################
    #에브리타임 로그인#

    idElem = browser.find_element(By.NAME, "userid")
    passwordElem = browser.find_element(By.NAME, "password")  # 비밀번호 입력
    loginElem = browser.find_element(
        By.XPATH, "//input[@value='로그인' ] | /input[@class='text']")

    # 아이디, 비밀번호 입력
    idElem.send_keys(id)
    passwordElem.send_keys(password)

    # 로그인 버튼 클릭
    loginElem.click()

    # 로그인 여부 검사 => 로그인 실패시 에러 발생
    if browser.current_url == 'https://everytime.kr/user/login':  # 로그인 실패
        browser.back()
        #로그인 실패 에러 발생
        raise loginError()

    return browser


def get_time_period(browser: WebDriver):
    """
    @param browser : 현재 사용되는 웹 드라이버
    @return time_period : 교시 및 top 정보가 엮여 있는 것
    각 교시가 언제 시작하는지는 해당 교시의 css 요소 중 top을 보면 알 수 있음.
    따라서 top 정보를 기반으로 몇교시인지 알 수 있도록 dict 을 이용한다.
    dict[top] => 해당 교시 정보
    """
    ##################################################################
    # 시간대 정보 가져오기
    times = browser.find_elements(By.XPATH, "//div[@class='hour']")
    time_period: dict[int, str] = {}
    for time in times:
        # 스타일 추출
        style = css_parser(time.get_attribute('style'))
    
        # 몇 교시인지 정보 추출        
        name = time.get_attribute('innerText').replace('교시', '')

        # (top :  교시) 형태로 dict에 값 넣음
        time_period[style['top']] = name
    return time_period


def get_lectures(browser: WebDriver, time_period: dict[int, str]):
    """
    @params browser 현재 https://everytime.kr/timetable 위치에 있는 브라우저
    @params time_period get_time_period로 얻은 top-시간표 사이의 대응 정보 
    """
    day_td: list[WebElement] = browser\
        .find_element(By.XPATH, "//table[@class='tablebody']")\
        .find_elements(By.TAG_NAME, 'td')[:-2]
    # 총 길이 7인데, 토, 일은 무시한다.

    lec_dict: dict[str, Lecture] = {}
    # lec_same으로 동일 과목 구분함!
    # Lecture 강의 정보 받음!

    day_count = 0  # 무슨 요일인지 세는 숫자. 0 부터 월요일

    for day in day_td:
        lectures: list[WebElement] = day.find_elements(
            By.CLASS_NAME, 'subject')
        for lec in lectures:
            # 과목 이름 가져오기
            lec_name = lec\
                .find_element(By.TAG_NAME, 'h3')\
                .get_attribute('innerText')

            # 교수님 이름 가져오기
            lec_prof = lec\
                .find_element(By.TAG_NAME, 'em')\
                .get_attribute('innerText')

            # 동일 과목인지 보기 위해 클래스 정보 가져오기
            lec_same = lec\
                .get_attribute('class').replace('subject', '').strip(' ')

            # 스타일 가져오기
            lec_style = lec.get_attribute('style')

            # 과목 정보가 없다면 과목 생성
            if lec_same not in lec_dict:
                lec_dict[lec_same] = Lecture(lec_name, lec_prof)

            # 스타일 파싱
            styles = css_parser(lec_style)

            # 시작 교시의 top 및 끝 교시(다음)의 top 저장
            start = styles['top']  # 시작 교시
            end = styles['top'] + styles['height'] - 1  # 끝난 다음 교시

            # 각 교시를 숫자로 파싱
            start_p = float(time_period[start]) \
                if len(time_period[start]) > 0 else 0
            # end는 끝난 다음 교시를 가리키므로, 0.5 빼서 원래 교시 가리키게 만든다
            end_p = float(time_period[end]) - 0.5 \
                if len(time_period[end]) > 0 else 0

            lec_dict[lec_same].add_loc(day_count, start_p, end_p)
        day_count += 1
    return lec_dict


def get_user_TT_info(id: str, password: str) -> list[Lecture]:
    browser = user_login(id, password)

    timetable = browser.find_element(
        By.XPATH, "//a[@href='/timetable']")  # 시간표 창 클릭
    timetable.click()
    browser.implicitly_wait(3)

    ##################################################################
    # 시간대 정보 가져오기
    time_period = get_time_period(browser)

    ##################################################################
    # 월화수목금 가져오기
    lec_dict = get_lectures(browser, time_period)

    browser.implicitly_wait(5)
    browser.close()

    return lec_dict.values()

def scrap_table_info():
    id = input("id 입력 :")
    password = input("패스워드 입력 :")
    lectures = get_user_TT_info(id, password)
    for lec in lectures:
        lec.get_lec_info()