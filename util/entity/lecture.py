class Lecture:
    '''
    @class Lecture
    @desc 각 강좌 정보를 담고 있는 클래스. 해당 강좌의 시간대 정보를 포함한다.
    '''
    name: str
    professor: str
    loc: list[tuple[int, float, float]]

    def __init__(self, name: str, professor: str):
        self.name = name
        self.professor = professor
        self.loc = []

    def __str__(self):
        return self.__lec_info()

    def add_loc(self, day: int, start: float, end: float):
        self.loc.append((day, start, end+0.5))

    def get_locs(self):
        print(self.loc)

    def __lec_info(self):
        __result = f"강의 : {self.name}, 교수님: {self.professor}, 강의(요일,시작,끝) : {self.loc}"
        return __result

    def get_lec_info(self):
        print(f"강의 : {self.name}, 교수님: {self.professor}, 강의(요일,시작,끝) : {self.loc}")

