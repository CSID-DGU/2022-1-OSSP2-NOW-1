from lecture import *
from scrap_table_info import *

aaa = []
lectures = get_user_TT_info("leeminsuok", "052978a")
for lec in lectures:
    aaa.append(lec.return_locs())
    print(lec.return_lec_info())

print(aaa)
print(aaa[0])
print(aaa[0][0])
print(aaa[0][0][0])
