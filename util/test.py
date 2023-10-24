from .detailed_cource_info import DetailedLecture
from .errormessage import ErrorMessage
from .http import get_tetro, get_scores, get_tetro_list, get_univs, set_score
from .entity.tetro_pool import TetroPool
from .entity.user_score import UserScore

# 테트로미노 풀 가져오기
# 테트로미노 풀의 id 값 받음
# 해당 테트로미노 풀이 존재한다면 code = 200
# 성공하면 list[DetailedLecture]
# game py 연동
code1, tetros = get_tetro(3)
if code1 == 200:
    tetros: list[DetailedLecture]
    print(tetros)
    for t in tetros:
        print(t.c_num, t.loc, t.name, t.note, t.professor)
else:
    tetros: ErrorMessage
    print(tetros.message)

# 경쟁모드 점수 받아오기
# 테트로미노 풀의 id 값 받음
# 해당 테트로미노 풀이 존재한다면 code = 200
# 이 경우 val 값은 list[UserScore] 이므로, 해당 클래스로 사용가능
# 경쟁모드 점수 출력에 사용
code, val = get_scores(1)
if code == 200:
    val: list[UserScore]
    for score in val:
        print(score.name, score.score)
        # 유저 이름, 유저 점수


# code, val = set_score(id=3, name='testtt', score=150)
# if code == 200:
#     print(val['message'])
# else:
#     print(val.message)

# 대학 정보 받아오기
# list[University] 반환
# 그대로 사용하면 됩니다
univs = get_univs()

for u in univs:
    print(u.id, u.name)
    # 대학 id, 이름
# 대학의 테트로미노 풀 리스트 반환
# 대학의 id 값 받음 ( univ.id )
# 성공하면 code == 200
# 성공하면 list[TetroPool] 반환

code, tetro_pools = get_tetro_list(univs[0].id)

if code == 200:
    tt: list[TetroPool] = tetro_pools
    # t 는 DetailedLecture
    for t in tt:
        print(t.id, t.name, t.description)
        # id, 이름, 설명
# 테트로미노 풀 id / 유저 name / score
# 항상 {message : str} 반환
code, result = set_score(10, 'testking', 150)
# 테트로미노 풀 id, 유저 이름, 유저 점수
print(result.message)
