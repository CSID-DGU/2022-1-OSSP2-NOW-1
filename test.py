from util.http import get_tetro, get_scores, set_score 


get_tetro(1)
print(get_scores(1))
code, val = set_score(id=3, name='testtt', score=150)
if code == 200:
    print(val['message'])
else:
    print(val.message)
print(get_scores(1))
