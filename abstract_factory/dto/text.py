from typing import List


class Text:

    def __init__(self, x: int, y: int, text: str, font_size: int):
        self.x: int = x
        self.y: int = y
        self.text: str = text
        self.font_size: int = font_size
        self.rows: List[List[str]] = [[text]]
