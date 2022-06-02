from time import sleep
from typing import Union
from functools import partial
from selenium.webdriver.common.by import By
from selenium import webdriver
# from selenium.webdriver.support.expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from util.css_parser import css_parser
from util.detailed_cource_info import DetailedLecture
from util.lecture import Lecture


# 크롬 드라이버 자동으로 설치해주는 매니저


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
    browser: WebDriver
    try:
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
    except Exception as e:
        # 크롬 브라우저가 없는 상황. 크롬 브라우저를 설치해달라는 메시지 전달.
        print("최신 크롬 브라우저를 설치해주세요!")
        return

    ############################################################################
    #사이트 지정 및 화면 사이즈 지정#
    browser.set_window_size(800, 960)  # 화면 사이즈 지정

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
        # 로그인 실패 에러 발생
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
            # 동일 과목에 대한 다른 분반 정보를 가져오는 방식.
            # lec_same 은 color~ 형태의 이름을 가져, 동일 이름의 교과목도 구분 가능.
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

            # 소수점으로 인해 발생하는 에러 검사
            if end in time_period:
                # 키 있으면 상관 없음
                pass
            elif (end + 1.0) in time_period:
                # end + 1.0 있으면
                end += 1.0
            elif (end - 1.0) in time_period:
                # end - 1.0 있으면
                end -= 1.0

            end_p = float(time_period[end]) - 0.5 \
                if len(time_period[end]) > 0 else 0

            lec_dict[lec_same].add_loc(day_count, start_p, end_p)
        day_count += 1
    return lec_dict


def get_all_tables(browser: WebDriver) -> list[WebElement]:
    """
    유저가 생성해 둔 모든 테이블 반환
    """
    data_from = browser.find_element(By.XPATH, "//div[@class='menu']")
    tables: list[WebElement] = data_from.find_elements(By.TAG_NAME, "li")

    for t in tables:
        if t.get_attribute('class') == 'extension':  # 시간표 만들기 창이면 클릭 안함
            tables.remove(t)

    return tables


def get_user_TT_info(id: str, password: str) -> dict[str, list[Lecture]]:
    '''
    유저의 시간표 정보를 가져오는 함수.
    '''
    browser = user_login(id, password)

    timetable = browser.find_element(
        By.XPATH, "//a[@href='/timetable']")  # 시간표 창 클릭
    timetable.click()
    sleep(2)
    browser.implicitly_wait(3)

    ##################################################################
    # 현재 학기의 모든 시간표 가져오기
    tables = get_all_tables(browser)

    ret_tables = {}  # 사용자가 만든 시간표들

    for t in tables:
        t.click()  # 시간표 클릭
        sleep(0.5)
        table_name = t.get_attribute('innerText')
        browser.implicitly_wait(1)  # 정보를 가져오기 위한 대기 시간
        ##################################################################
        # 시간대 정보 가져오기
        time_period = get_time_period(browser)

        ##################################################################
        # 월화수목금 가져오기
        lec_dict = get_lectures(browser, time_period)
        ret_tables[table_name] = lec_dict.values()

    browser.implicitly_wait(3)
    browser.close()

    return ret_tables

###################학기 과목 정보 관련 코드들######################


def get_lecture_from_tr(tr: WebElement):
    '''
    WebElement tr 태그에서 상세한 수업 내용을 파싱, DetailedLecture 로 반환한다.
    '''
    print(tr.get_attribute('innerText'))
    infos: list[WebElement] = tr.find_elements(By.TAG_NAME, 'td')
    print(len(infos))
    target = [2, 3, 4, 8, 12]  # 가져올 데이터들
    # 학수강좌번호 / 교과목명 / 교원명 / 시간 / 비고
    text_infos: list[str] = []  # 가져온 데이터들
    for idx in target:
        temp = infos[idx].get_attribute('innerText')  # 텍스트 가져오기
        text_infos.append(temp)
    # 결과로 0 ~ 4 에 데이터 들어감

    c_num = text_infos[0]  # 학수강좌번호
    name = text_infos[1]  # 교과목명
    professor = text_infos[2]  # 교원명
    t = text_infos[3]  # 강의 시간
    note = text_infos[4]  # 비고

    dl = DetailedLecture(c_num, name, professor, t, note)

    return dl


def get_lectures_from_semester(browser: WebDriver, path: list[str]):
    '''
    에브리타임 사이트 상의 "수업 목록에서 검색" 버튼 등을 검사하여
    실제로 정보를 가져온다.
    '''
    search_button: WebElement
    # 검색 버튼 (수업 목록에서 검색)
    category: WebElement
    # 전공/영역: 전체 버튼

    try:
        search_button = browser.find_element(
            By.XPATH, "//li[@class='button search']")
    except:  # 수업 목록에서 검색 버튼이 없는 경우. (여름 학기나 겨울 학기 등)
        search_button = None

    if search_button:  # 버튼이 있다면
        search_button.click()  # 클릭
        WebDriverWait(browser, timeout=10).until(lambda d: d.find_element(
            By.XPATH, '//div[@class="list"]/table/tbody/tr'))

        # 리스트 데이터가 존재할 때까지 대기...
        try:
            category = browser.find_element(
                By.XPATH, "//span[text() = '전공/영역:']")  # 카테고리
        except:  # 카테고리 자체가 없는 경우도 존재함...
            print("no category")
            category = None

        if category:  # 카테고리가 있다면
            category.click()

            # try:
            for p in path:  # 전공/영역에서 경로 이동.
                elem = browser.find_element(By.XPATH, f"//li[text() ='{p}']")
                browser.implicitly_wait(2)
                elem.click()

            sleep(2)
            WebDriverWait(browser, timeout=5).until(lambda d: d.find_element(
                By.XPATH, '//div[@class="list"]/table/tbody/tr'))  # 리스트 내용이 나올 때까지 대기
            lec_list = browser.find_element(By.XPATH, '//div[@class = "list"]')
        #     # 브라우저 상에 강의 리스트 설정
            while True:
                # height = browser.execute_script('return arguments[0].scrollHeight;', lec_list)
                # print(height)
                # 높이가 차이가 나는지 검색해보기 위함.

                browser.execute_script(
                    'arguments[0].scrollBy(0, arguments[0].scrollHeight);', lec_list)  # 스크롤
                sleep(3)  # 정보 로딩될 때까지 대기
                cond = browser.find_element(
                    By.XPATH, '//div[@class="list"]/table/tfoot').get_attribute('style')  # 끝까지 읽는 조건
                if cond == 'display: none;':  # 끝까지 읽었으면
                    break  # 그만
            # 실제 강의 리스트들 가져오기
            detailed_lectures_raw: list[WebElement] = lec_list.find_element(By.TAG_NAME, 'tbody')\
                .find_elements(By.TAG_NAME, 'tr')

            detailed_lectures: list[DetailedLecture] = []

            for lec in detailed_lectures_raw:
                dl = get_lecture_from_tr(lec)  # detailed lecture 반환
                detailed_lectures.append(dl)  # 삽입

            return detailed_lectures
    # 실패하면 아무것도 반환 안함.


def get_semester(browser: WebDriver, target: str):
    '''
    get_semesters 함수 내에서 사용하는 함수. 특정 학기에 대한 WebElement을 가져오는데 사용한다.

    @params target selector로부터 target 이름을 가진 WebElement을 반환한다.


    입력받은 원소가 없으면 에러난다 ...
    '''
    try:
        target_semester = browser.find_element(
            By.XPATH, f'//select[@id="semesters"]/option[text()="{target}"]')
        return (target, target_semester)
    except:  # 값이 존재하지 않는 경우.
        return (target, None)


def get_semesters(browser: WebDriver, target: list[str]):
    '''
    선택한 강의들과 
    @params browser 인터넷 브라우저
    @params target 대상이 되는 학기들 (ex ["2022년 1학기", "2021년 2학기"])
    '''
    # selector : 학기를 의미하는 버튼
    selector = browser.find_element(By.XPATH, "//select[@id='semesters']")

    get_semester_from_browser = partial(get_semester, browser)
    target_semesters: list[tuple[str, Union[WebElement, None]]] = list(
        map(get_semester_from_browser, target))

    # 검색 안되는 학기가 있다면 삭제한다.
    for v in target_semesters:
        if v[1] == None:  # Element 값
            target_semesters.remove(v)

    # 결과 반환
    return selector, target_semesters


def get_lectures_info(id: str, password: str, target: list[str], path: list[str]):
    '''
    @params id 유저 아이디
    @params password 유저 비밀번호
    @params target 대상이 되는 학기들 (ex ["2022년 1학기", "2021년 2학기"])
    @params path 전공 영역에서 클릭하는 경로 (ex ["전공", "공과대학", "컴퓨터공학전공"])
    '''

    browser = user_login(id, password)  # 로그인

    timetable = browser.find_element(
        By.XPATH, "//a[@href='/timetable']")  # 시간표 창 클릭
    timetable.click()  # 클릭
    browser.implicitly_wait(3)  # 3초 대기

    select, semesters = get_semesters(browser, target)
    # 모든 학기의 모든 강좌 리스트.
    lectures_all_semesters: dict[str, list[DetailedLecture]] = {}
    # 가져온 학기 목록 출력
    for semester in semesters:
        print(semester[0])

        select.click()
        browser.implicitly_wait(1)
        # 학기 선택 select 클릭

        semester[1].click()
        browser.implicitly_wait(1)
        # 해당 학기 클릭

        dls = get_lectures_from_semester(browser, path)  # 상세강좌정보들
        if dls != None:
            lectures_all_semesters[semester[0]] = dls  # 학기를 키로 써서 상세강좌정보 삽입

    return lectures_all_semesters


if __name__ == "__main__":
    # try :
    id = input("id 입력 :")
    password = input("패스워드 입력 :")
    # tables = get_user_TT_info(id, password)
    # # 정보를 잘 스크래핑 했는지 검사
    # for name in tables :
    #     print(name)
    #     for lec in tables[name]:
    #         lec.get_lec_info()
    #     print()
    target = ['2022년 1학기', '2021년 2학기']
    path = ["전공", "공과대학", "컴퓨터공학전공"]
    all_lectures = get_lectures_info(id, password, target, path)

    for semester in all_lectures:
        print(f"학기: {semester}\n")
        for lec in all_lectures[semester]:  # 각 강좌 정보 출력
            print(lec)
# except Exception as e:
    # print(e)
