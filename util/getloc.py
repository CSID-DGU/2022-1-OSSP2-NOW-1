from .scrap_table_info import *

lec_locs : list[list[list[int, float,float]]] = []
lec_name = []
lec_professor = []
id = 0
password = 0

#전역변수들
wide = 0 #가로길이
height = 0 #세로길이
in_height = 0 #안쪽 세로길이
interval = 0 #끝시간 - 끝시간
block_a = []
block_a_size = 0
lec_time : list[int] = []
B_DATA = []
BLOCK_DATA = []

def get_interval():
    lec_locs

#강의 시간표 가져오기
def get_lectures_info():

    id = input("id 입력 :")
    password = input("패스워드 입력 :")
    lectures = get_user_TT_info(id, password)
    for lec in list(lectures.values())[0]:
        lec_locs.append(lec.loc)
        lec_name.append(lec.name)
        lec_professor.append(lec.professor)
        
def make_block_data(i):
    B_DATA = []
    COUNT = 1 + i
    if (len(lec_locs[i]) == 1):
        block_a = []
        block_a_size = int(abs(lec_locs[i][0][1] - lec_locs[i][0][2]) + 0.5)
       
        block_a = [0 for _ in range(block_a_size**2)]
        
        for i in range(0, block_a_size):
            lec_time.append(i * block_a_size)
        for i in range(0, len(lec_time)):
            a = lec_time.pop()
            for g in range(0, int(block_a_size * block_a_size)):
                if (g == a):
                    block_a[g] = COUNT

        print_block(block_a, block_a_size)
        for i in range (0, 4):
            B_DATA.append(block_a)
        BLOCK_DATA.append(B_DATA)

    elif (len(lec_locs[i]) == 2) :
        wide = abs(lec_locs[i][0][0] - lec_locs[i][1][0]) + 1  # 가로길이
        height = abs(lec_locs[i][0][1] - lec_locs[i][1][2])  # 세로길이
        in_height = abs(lec_locs[i][0][2] - lec_locs[i][1][1])  # 안쪽 세로길이
        interval = int(abs(lec_locs[i][0][2] - lec_locs[i][1][2]) + 0.5)  # 끝 - 끝
        f_lec = int(abs(lec_locs[i][0][1] - lec_locs[i][0][2]) + 0.5)  # 앞 수업 길이
        b_lec = int(abs(lec_locs[i][1][1] - lec_locs[i][1][2]) + 0.5)  # 뒷 수업 길이

        block_a = []
        block_a_size = max(height, in_height, wide)
        for i in range(0, int(block_a_size * block_a_size)):
            block_a.append(0)
        make_lec_time(block_a, block_a_size, lec_time, wide, height, in_height, interval, f_lec, b_lec)
        print(lec_time)

        for i in range(0, len(lec_time)):
            a = lec_time.pop()
            for g in range(0, int(block_a_size * block_a_size)):
                if (g == a):
                    block_a[g] = COUNT

        print_block(block_a, block_a_size)
        for i in range(0, 4):
            B_DATA.append(block_a)
        BLOCK_DATA.append(B_DATA)

def make_lec_time(block_a, block_a_size, lec_time, wide, height, in_height, interval, f_lec, b_lec) :
    for i in range (0, f_lec) :
        lec_time.append(int(block_a_size * i))
    for i in range (interval, interval+b_lec) :
        lec_time.append(int(block_a_size * i + wide-1))
    #for i in range (0, len(lec_time)) :
    #    if ( block_a_size * block_a_size < lec_time[i] ) :
    #        lec_time[i] = lec_time[i] - (block_a_size * block_a_size - block_a_size)

def print_block(block_a, block_a_size) :
    for i in range(0, int(block_a_size * block_a_size)):
        print(block_a[i], end=", ")
        if (i % block_a_size == block_a_size - 1):
            print()

def getloc():
    get_lectures_info()
    # 가져온 강의 체크용
    print(lec_locs[0])  # 수업 시간 전부, 이 숫자로 수업구분
    print(lec_locs[0][0])  # 수업 하나
    print(lec_locs[0][0][0])  # 0요일 1시작 2끝

    for i in range(0, len(lec_locs)):
        print(lec_name[i])
        make_block_data(i)
    print(BLOCK_DATA)
    print(BLOCK_DATA[1])
    print(BLOCK_DATA[1][0])
    return BLOCK_DATA
