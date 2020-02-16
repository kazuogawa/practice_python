from abstract_factory.diagram.diagram_factory import DiagramFactory
from abstract_factory.diagram.svg_diagram import SvgDiagram


class SvgDiagramFactory(DiagramFactory):
    def make_diagram(self, width: int, height: int) -> SvgDiagram:
        return SvgDiagram(width, height)
