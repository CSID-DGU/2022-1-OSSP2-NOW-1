class University:
    '''
    @class University
    @desc 대학을 의미하는 클래스
    '''
    id: int
    name :str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name