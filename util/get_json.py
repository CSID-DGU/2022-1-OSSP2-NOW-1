'''
스크래핑 한 데이터들을 json 으로 가공하기 위한 파일.
'''

import json
from .scrap_table_info import get_lectures_info

if __name__ == '__main__':
    id = input("id 입력 :")
    password = input("패스워드 입력 :")

    target = ['2022년 1학기', '2021년 2학기']
    path = ["전공", "공과대학", "컴퓨터공학전공"]
    all_lectures = get_lectures_info(id, password, target, path)

    for semester in all_lectures:
        print(f"학기: {semester}\n")
        for lec in all_lectures[semester]:  # 각 강좌 정보 출력
            print(lec)

    for semester in all_lectures:
        for i in range(len(all_lectures[semester])):
            all_lectures[semester][i] = all_lectures[semester][i].__dict__
            print(all_lectures[semester][i])
            # json 파싱하기 위해 클래스를 딕셔너리 형태로 변환

    with open('lectures.txt', 'w+', encoding='utf8') as f:
        json.dump(all_lectures, f, ensure_ascii=False)
