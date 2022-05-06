from lecture import *
from scrap_table_info import *
import math

aaa = []
bbb = []
ccc = []
lectures = get_user_TT_info("leeminsuok", "052978a")
for lec in lectures:
    aaa.append(lec.return_locs())
    bbb.append(lec.return_name())
    ccc.append(lec.return_professor())
aaa[0] = aaa[4]
print(aaa[0]) #수업 시간 전부, 이 숫자로 수업구분
print(aaa[0][0]) #수업 하나
print(aaa[0][0][0]) #0요일 1시작 2끝

wide = abs(aaa[0][0][0] - aaa[0][1][0]) + 1  #가로길이
height = abs(aaa[0][0][1] - aaa[0][1][2])  #세로길이
in_height = abs(aaa[0][0][2] - aaa[0][1][1])
f_lec = int(abs(aaa[0][0][1] - aaa[0][0][2])) #앞 수업 길이
b_lec = int(abs(aaa[0][1][1] - aaa[0][1][2])) #뒷 수업 길이


block_a = []
block_a_size = 0
if ( wide > height ) :
    block_a_size = wide
else :
    block_a_size = height

for i in range (0, int(block_a_size * block_a_size)) :
    block_a.append(0)

lec_time = []

def make_lec_time() :
    for i in range (0, f_lec) :
        lec_time.append(block_a_size * i)
    for i in range (f_lec, f_lec+b_lec) :
        lec_time.append(block_a_size * (i+in_height) + wide-1)

make_lec_time()
print(lec_time)

for i in range (0, int(block_a_size * block_a_size)) :
    for g in lec_time :
        if (i == g) :
            block_a[i] = 1

#print(block_a)
for i in range (0, int(block_a_size * block_a_size)) :
    print(block_a[i], end= ", ")
    if (i%block_a_size == block_a_size-1) :
        print()