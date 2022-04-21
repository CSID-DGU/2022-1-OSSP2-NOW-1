from lecture import *
from scrap_table_info import *

aaa = []
bbb = []
ccc = []
lectures = get_user_TT_info("leeminsuok", "052978a")
for lec in lectures:
    aaa.append(lec.return_locs())
    bbb.append(lec.return_name())
    ccc.append(lec.return_professor())

print(aaa)
print(bbb)
print(ccc)

print(aaa[0]) #수업 시간 전부, 이 숫자로 수업구분
print(aaa[0][0]) #수업 하나
print(aaa[0][0][0]) #0요일 1시작 2끝

for i in (0,10) :
    print(aaa[i])
    print(bbb[i])
    print(ccc[i])