from abstract_factory.dto.color import Color
from abstract_factory.dto.delimiter import Delimiter

from typing import List


class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int, fill: Color, stroke: Color):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.fill: Color = fill
        self.stroke: Color = stroke
        self.rows: List[List[Delimiter]] = self._create_rectangle()

    def _create_rectangle(self) -> List[List[Delimiter]]:
        fill_delimiter: Delimiter = Delimiter.BLANK if self.fill == Color.WHITE else Delimiter.PAR
        rows = [[fill_delimiter for _ in range(self.width)] for _ in range(self.height)]
        for wx in range(1, self.width - 1):
            rows[0][wx]: Delimiter = Delimiter.HORIZONTAL
            rows[self.height - 1][wx]: Delimiter = Delimiter.HORIZONTAL
        for y in range(1, self.height - 1):
            rows[y][0]: Delimiter = Delimiter.VERTICAL
            rows[y][self.width - 1]: Delimiter = Delimiter.VERTICAL
        for y, x in ((0, 0), (0, self.width - 1), (self.height - 1, 0),
                     (self.height - 1, self.width - 1)):
            rows[y][x]: Delimiter = Delimiter.CORNER
        return rows
