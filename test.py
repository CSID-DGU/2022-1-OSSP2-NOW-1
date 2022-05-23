from util.lecture import Lecture
from util.scrap_table_info import get_user_TT_info

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

    all_lectures: dict[str, list[Lecture]]
    all_lectures = get_user_TT_info(id, password)

    for lec in all_lectures:
        print(lec)
        for l in all_lectures[lec]:
            print(l.loc)