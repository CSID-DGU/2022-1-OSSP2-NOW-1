from lecture import *
from scrap_table_info import *

lec_locs = []
lec_name = []
lec_professor = []
lectures = get_user_TT_info("leeminsuok", "052978a")

#강의 시간표 가져오기
for lec in lectures:
    lec_locs.append(lec.return_locs())
    lec_name.append(lec.return_name())
    lec_professor.append(lec.return_professor())

lec_locs[0]

#가져온 강의 체크용
print(lec_locs[0]) #수업 시간 전부, 이 숫자로 수업구분
print(lec_locs[0][0]) #수업 하나
print(lec_locs[0][0][0]) #0요일 1시작 2끝

#전역변수들
wide = 0 #가로길이
height = 0 #세로길이
in_height = 0 #안쪽 세로길이
interval = 0 #끝시간 - 끝시간
f_lec = 0 # 앞 수업 길이
b_lec = 0 # 뒷 수업 길이
block_a = []
block_a_size = 0
block_a_size = 0
lec_time = []

def make_lec_time() :
    for i in range (0, f_lec) :
        lec_time.append(int(block_a_size * i))
    for i in range (0, b_lec) :
        lec_time.append(int(block_a_size * (i+interval) + wide-1))
    for i in range (0, len(lec_time)) :
        if ( block_a_size * block_a_size < lec_time[i] ) :
            lec_time[i] = lec_time[i] - (block_a_size * block_a_size - block_a_size)

def make_block_data(i) :
    wide = abs(lec_locs[i][0][0] - lec_locs[i][1][0]) + 1  # 가로길이
    height = abs(lec_locs[i][0][1] - lec_locs[i][1][2])  # 세로길이
    in_height = abs(lec_locs[i][0][2] - lec_locs[i][1][1])  # 안쪽 세로길이
    interval = abs(lec_locs[i][0][2] - lec_locs[i][1][2])  # 끝 - 끝
    f_lec = int(abs(lec_locs[i][0][1] - lec_locs[i][0][2]) + 0.5)  # 앞 수업 길이
    b_lec = int(abs(lec_locs[i][1][1] - lec_locs[i][1][2]) + 0.5)  # 뒷 수업 길이

    block_a = []
    block_a_size = max(height, in_height, wide)
    for i in range(0, int(block_a_size * block_a_size)):
        block_a.append(0)

    make_lec_time()
    print(lec_time)

    for i in range(0, int(block_a_size * block_a_size)):
        for g in lec_time:
            if (i == g):
                block_a[i] = 1

def print_block() :
    for i in range(0, int(block_a_size * block_a_size)):
        print(block_a[i], end=", ")
        if (i % block_a_size == block_a_size - 1):
            print()

def append_block_data(BLOCK_DATA) :
    BLOCK_DATA.append(block_a)


for i in range (0, len(lec_locs)) :
    make_block_data(i)
    print_block()
