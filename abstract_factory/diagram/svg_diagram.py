# TODO: 後でconfig parser作って入れておく
SVG_SCALE = 20
class SvgDiagram:
    def __init__(self, width: int, height:int):
        self.px_width: int = width * SVG_SCALE
        self.px_height: int = height * SVG_SCALE
