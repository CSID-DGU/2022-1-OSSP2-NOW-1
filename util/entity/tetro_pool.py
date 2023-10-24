class TetroPool:
    '''
    @class TetroPool
    @desc 테트로미노 풀을 의미하는 클래스. 경쟁 모드의 테트로미노 풀을 의미한다.
    '''
    id : int
    name : str
    description : str

    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description