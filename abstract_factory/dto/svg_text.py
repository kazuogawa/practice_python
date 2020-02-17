from abstract_factory.repository.config_repository import ConfigRepository


class SvgText:
    def __init__(self, x: int, y: int, font_size: int, text: str):
        config_repository = ConfigRepository()
        self.x = x * config_repository.svg_scale
        self.y = y * config_repository.svg_scale
        self.font_size = font_size * config_repository.svg_scale
        # 関係ないsvg_scaleを渡しても問題ないらしい
        self.svg = config_repository.svg_text.format(**locals())
