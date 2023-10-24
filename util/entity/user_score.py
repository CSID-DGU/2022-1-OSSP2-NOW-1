class UserScore:
    '''
    @class UserScore
    @desc 유저 점수 정보를 담고 있는 클래스

    @field name : 이름
    @field score : 유저의 점수
    '''

    name: str
    score : int

    def __init__(self, name: str, score: str):
        self.name = name
        self.score = score