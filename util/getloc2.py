from util.http import get_tetro
from util.lecture import Lecture
from util.rotate_block import idx2loc, rotate_block, print_square
from util.scrap_table_info import get_user_TT_info


def round_05(var: float):
    '''
    0.5 더해서 int로 자르기
    '''
    return int(var + 0.5)

def make_block_data(lectures: list[Lecture]):
    '''
    block data를 만들어서 반환.
    '''
    BLOCK_DATA = []
    block_id = 3 # 처음 블럭의 id를 3으로 임의대로 지정한다. 테두리 블럭을 1로 설정했음
    for lecture in lectures:
        loc = lecture.loc

        start_time = 100  # 임시 값. 100교시는 없음.
        stop_time = 0  # 마지막 시간대
        start_day = 100  # 시작 요일
        stop_day = 0  # 끝 요일

        for lec_time in loc:  # 하나의 강의에 대한 시간들
            start_time = min(start_time, lec_time[1])  # 시작 시간
            stop_time = max(stop_time, lec_time[2])  # 끝 시간
            start_day = min(start_day, lec_time[0])
            stop_day = max(stop_day, lec_time[0])
        
        # start / stop time을 정수형으로 수정
        start_time = round_05(start_time)
        stop_time = round_05(stop_time)
              
        width = stop_day - start_day + 1
        height = stop_time - start_time

        R = height - width #보정 계수
        base = height if R > 0 else width

        block = get_0block(base)  # 0으로 채운 블럭 생성
        indices = get_normal_indices(loc,R,start_day,start_time,base)

        for idx in indices:
            block[idx] = block_id # 인덱스 삽입하기.
        
        block_4 : list[list[int]] = []
        #블럭 4방향 가지도록.
        print(lecture.name)
        print_square(block)
        for _ in range(4):
            block_4.append(block)
            block = rotate_block(block)
        
        BLOCK_DATA.append(block_4)
        block_id += 1
    
    return BLOCK_DATA

def get_normal_indices(loc : list[tuple[int,float,float]], R: int, start_day: int, start_time: int, base: int):
    '''
    @description 실제 보정 작업을 수행하고, 인덱스들을 반환하는 함수.
    @params lec 강의 인스턴스
    @params R 보정 계수. R > 0 -> 가로로 보정 / R < 0 -> 세로로 보정
    @params start_day 가로 좌표 기준
    @params start_time 세로 좌표 기준
    @params base 한 변의 최대 길이
    '''
    
    r_cor = int(abs(R/2)) # 실제로 보정하는 수치.
    cor_idx: list[int] = [] # 나중에 반환할 배열
    for d, st, ed in loc:
        ### 기준점 보정
        st = round_05(st) - start_time # 정수화 + 기준점 보정
        ed = round_05(ed) - start_time # 정수화 + 기준점 보정
        x = d - start_day # x축 기준점 보정해서 결과 얻기

        y_list = [t for t in range(st, ed)] # y축 기준점들 얻기.

        ### 보정 계수에 의한 보정
        if R > 0: # 세로로 더 길면 가로로 보정.
            x = x + r_cor
        else : # 가로로 더 길면 세로로 보정.
            for i in range(len(y_list)):
                y_list[i] += r_cor
        
        ### 인덱스 생성
        for y in y_list:
            loc = idx2loc(y, x, base)
            cor_idx.append(loc)
    
    return cor_idx # 전체 인덱스 반환

def get_0block(base: int):
    '''
    0으로 채운 배열 반환.
    '''
    return [0 for _ in range(base**2)]

def getloc2(lecture:Lecture):
    return lecture, make_block_data(lecture)

def get_lectures_info():
    id = input("id 입력 :")
    password = input("패스워드 입력 :")
    lectures =  get_user_TT_info(id, password)
    return lectures


def get_blocks_personal(id: str, password: str, lec_id: int):
    '''
    개인모드용
    '''
    lectures =  get_user_TT_info(id, password)
    lec_names = list(lectures.keys())
    print("인덱스 선택")
    name = lec_names[lec_id]
    cur_lecture = list(lectures[name])
    return getloc2(cur_lecture)

def get_blocks_competition(id: int):
    '''
    경쟁모드용
    '''
    code, lectures = get_tetro(id)
    if code == 200:
        return getloc2(lectures)