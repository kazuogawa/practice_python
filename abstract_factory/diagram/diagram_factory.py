from abstract_factory.diagram.diagram import Diagram
from abstract_factory.dto.text import Text
from abstract_factory.dto.rectangle import Rectangle
from abstract_factory.dto.color import Color


class DiagramFactory:
    @classmethod
    def make_diagram(cls, width: int, height: int) -> Diagram:
        return Diagram(width, height)

    @classmethod
    def make_rectangle(cls, x: int, y: int, width, height, fill=Color.WHITE, stroke=Color.BLACK) -> Rectangle:
        return Rectangle(x, y, width, height, fill, stroke)

    @classmethod
    def make_text(cls, x: int, y: int, text: str, font_size=12) -> Text:
        return Text(x, y, text, font_size)
