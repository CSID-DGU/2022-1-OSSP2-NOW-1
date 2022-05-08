import string
from util.lecture import Lecture


class DetailedLecture(Lecture):
    '''
    강좌에 대한 상세 정보 저장

    에타의 정보는 학년 / 구분/ 학수강좌번호 / 교과목명 / 교원명 / 학점 / 이론 / 실습 / 시간 / 강의실 / 강의평 / 담은 인원 / 비고

    총 13개의 tr이 있는데, 여기서 학수강좌번호 / 교과목명 / 교원명 / 시간 / 비고 를 저장

    추가된 것은 강좌번호 / 비고
    '''
    c_num: string  # 학수강좌번호
    note: string  # 비고

    def __init__(self, c_num: str, name: str, professor: str, t: str, note: str):
        self.c_num = c_num  # 학수 번호
        self.note = note  # 비고
        super().__init__(name, professor)  # 과목 이름 / 교수
        self.parse_time(t)

    def parse_time(self, t: str):
        # 수5.0-6.5/13:00-15:00,목2.0-3.5/10:00-12:00
        if len(t.strip()) == 0:  # 문자열이 없으면
            return  # 아무것도 안한다.

        times = t.split(',')  # 컴마 기준으로 우선 나눔. (날짜별)
        for temp in times:
            time, _ = temp.split('/')  # 요일:교시 정보만 얻어온다.
            dow = time[0]  # 요일
            dow_int = -1  # int 형으로 나타나는 요일
            match dow:
                case '월':
                    dow_int = 0
                case '화':
                    dow_int = 1
                case '수':
                    dow_int = 2
                case '목':
                    dow_int = 3
                case '금':
                    dow_int = 4
                case '토':
                    dow_int = 5
                case '일':
                    dow_int = 6

            start, end = [float(x) for x in time[1:].split('-')]  # 시작시간 및 끝시간
            self.add_loc(dow_int, start, end)

    def __lec_info(self):
        __result = f"학수강좌번호: {self.c_num}, 강의 : {self.name}, 교수님: {self.professor}, 강의(요일,시작,끝) : {self.loc} \n\t 비고: {self.note}"
        return __result
    
    def __str__(self):
        return self.__lec_info()