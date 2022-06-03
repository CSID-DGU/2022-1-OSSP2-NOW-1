from typing import Union
import json
import requests as req
from util.detailed_cource_info import DetailedLecture
from util.errormessage import ErrorMessage
from util.tetro_pool import TetroPool
from util.university import University
from util.user_score import UserScore

# 기본 경로
baseUrl = 'http://ttpang.site'

# get 메서드용 헤더
headers_get = {'Accept': 'application/json'}
# post 메서드용 헤더
headers_post = {'Content-Type': 'application.json'}

'''
@에러 메시지를 가져온다. 
'''


def get_error_message(err: req.Response):
    target: dict = json.loads(err.text)['message']
    err_message = ErrorMessage(target)
    return (err.status_code, err_message)


'''
@테트로미노 풀을 가져온다.
@error : 에러 메시지 반환
'''


def get_tetro(id: Union[int, str]):
    res = req.get(f'{baseUrl}/api/tetro/get-tetro/{id}', headers=headers_get)
    target = json.loads(res.text)

    if res.status_code == 200:
        result: list[DetailedLecture] = []

        for lec in target:
            _lec = DetailedLecture(
                c_num=lec['c_num'],
                name=lec['name'],
                professor=lec['professor'],
                note=lec['note']
            )

            lec_times: list[int, str, str] = lec['loc']

            for loc in lec_times:
                _lec.add_loc(loc[0], float(loc[1]), float(loc[2]))
            result.append(_lec)
        return (res.status_code, result)
    else:
        return get_error_message(res.text)


'''
@테트로미노 점수를 가져온다.
@error 에러 메시지 반환
'''


def get_scores(id: Union[int, str]):
    res = req.get(f'{baseUrl}/api/tetro/get-scores/{id}', headers=headers_get)
    if res.status_code == 200:
        us_list: list[UserScore] = []
        target = json.loads(res.text)

        for t in target:
            us = UserScore(t['name'], t['score'])
            us_list.append(us)

        return (res.status_code, us_list)  # 무조건 배열 반환


'''
@유저 점수를 받아온다.
@params id : 테트로미노 풀의 id
@params name : 유저의 이름
@params score : 유저의 점수

# 성공하면 message 가 있는 dict 로 반환된다. {message : ~}
@error 에러 메시지 반환
'''


def set_score(id: Union[int, str], name: str, score: int):

    res = req.post(f'{baseUrl}/api/tetro/set-score/{id}', headers=headers_post, json={
        "name": name,
        "score": score
    })

    target = json.loads(res.text)

    if res.status_code == 200:
        return (res.status_code, target)
    else:
        return get_error_message(res)


'''
@사용 가능한 대학 목록을 가져온다. 해당 목록에서 인덱스를 추출, 해당 인덱스 기반으로 사용가능한 테트로미노 풀에 접근한다.

'''


def get_univs():
    res = req.get(f'{baseUrl}/api/info/univs', headers=headers_get)
    target = json.loads(res.text)

    univs: list[University] = []

    if res.status_code == 200:
        for t in target:
            univ = University(t['id'], t['name'])
            univs.append(univ)

    return univs


'''
@사용 가능한 풀 목록 정보를 가져온다.

@error 에러 메시지 반환
'''


def get_tetro_list(id: Union[int, str]):
    res = req.get(f'{baseUrl}/api/info/{id}/tetro-pools', headers=headers_get)
    target = json.loads(res.text)

    if res.status_code == 200:
        tetro_pools: list[TetroPool] = []

        for t in target:
            tp = TetroPool(t['id'], t['name'], t['description'])
            tetro_pools.append(tp)
        return (res.status_code, tetro_pools)
    else:
        return get_error_message(res)
