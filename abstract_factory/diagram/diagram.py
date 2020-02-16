from typing import Union
from collections import defaultdict
from abstract_factory.dto.text import Text
from abstract_factory.dto.rectangle import Rectangle


class Diagram:
    def __init__(self, width: int, height: int):
        # TODO:ここ謎なのでdefaultdictにしておく
        self.diagram = defaultdict(list)
        self.width = width
        self.height = height

    def add(self, component: Union[Text, Rectangle]):
        for y, row in enumerate(component.rows):
            for x, char in enumerate(row):
                self.diagram[y + component.y][x + component.x] = char

    # TODO:後で何かしら書き出す処理つくる
    def save(self, filename: str):
        print('save complete!')
