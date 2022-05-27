from util.detailed_cource_info import DetailedLecture
from util.errormessage import ErrorMessage
from util.http import get_tetro, get_scores, get_tetro_list, get_univs, set_score
from util.tetro_pool import TetroPool
from util.user_score import UserScore 


code1, tetros = get_tetro(3)
if code1 == 200:
    tetros : list[DetailedLecture]
    print(tetros)
    for t in tetros:
        print(t.c_num,t.loc, t.name, t.note, t.professor)
else :
    tetros: ErrorMessage
    print(tetros.message)


code, val = get_scores(1)
if code == 200:
    val : list[UserScore]
    for score in val:
        print(score.name, score.score)
        
# code, val = set_score(id=3, name='testtt', score=150)
# if code == 200:
#     print(val['message'])
# else:
#     print(val.message)

univs = get_univs()

for u in univs :
    print(u.id, u.name)

code, tetro_pools = get_tetro_list(univs[0].id)

if code == 200:
    tt : list[TetroPool] = tetro_pools
    # t 는 DetailedLecture
    for t in tt:
        print(t.id, t.name, t.description)

code, result = set_score(10, 'testking', 150)
print(result.message)