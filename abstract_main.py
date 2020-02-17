from abstract_factory.diagram.diagram_factory import DiagramFactory
from abstract_factory.diagram.svg_diagram_factory import SvgDiagramFactory
from abstract_factory.diagram.diagram import Diagram


def create_diagram(factory: DiagramFactory):
    diagram: Diagram = factory.make_diagram(30, 7)
    # rectangle ... 矩形(くけい)
    rectangle = factory.make_rectangle(x=4, y=1, width=22, height=5, fill="yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram


def main():
    text_filename = 'sample_text_filename'
    txt_diagram: Diagram = create_diagram(DiagramFactory())
    txt_diagram.save(text_filename)
    svg_filename = 'sample_svg_filename'
    svg_diagram: Diagram = create_diagram(SvgDiagramFactory())
    svg_diagram.save(svg_filename)


if __name__ == '__main__':
    main()
