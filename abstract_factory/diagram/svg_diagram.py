from abstract_factory.repository.config_repository import ConfigRepository
from typing import List


class SvgDiagram:
    def __init__(self, width: int, height: int):
        config_repository = ConfigRepository()
        self.px_width: int = width * config_repository.svg_scale
        self.px_height: int = height * config_repository.svg_scale
        self.diagram: List[str] = [config_repository.svg_start.format(**locals())]

    def add(self, component):
        self.diagram.append(component.svg)
