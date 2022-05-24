from typing import Union

class ErrorMessage :
    message : Union[str, list[str]]

    def __init__(self, message: Union[str, list[str]]):
        self.message = message