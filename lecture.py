from typing import List


class Lecture:
    name: str
    professor: str
    loc: List[tuple[int, str]]

    def __init__(self, name: str, professor: str):
        self.name = name
        self.professor = professor
        self.loc = []

    def add_loc(self, day: int, start: float, end: float):
        self.loc.append((day, start, end))

    def get_locs(self):
        print(self.loc)

    def get_lec_info(self):
        print(f"강의 : {self.name}, 교수님: {self.professor}, 강의(요일,시작,끝) : {self.loc}")
