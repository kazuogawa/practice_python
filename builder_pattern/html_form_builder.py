from html import escape
from builder_pattern.abstract_form_builder import AbstractFormBuilder
from typing import Dict, Optional, List, Any, Union
from collections import defaultdict


class HtmlFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.title = "HtmlFormBuilder"
        # 何でもかんでもrow, columnをkeyにして入れてもいいのか・・・・？
        self.items: Dict[(int, int), str] = defaultdict()

    def form(self) -> str:
        html: List[str] = ["<!doctype html>\n<html><head><title>{}</title></head>"
                           "<body>".format(self.title), '<form><table border="0">']
        this_row: Optional[int] = None
        for key, value in sorted(self.items.items()):
            row: int
            column: int
            row, column = key
            if this_row is None:
                html.append(" <tr>")
            elif this_row != row:
                html.append(" </tr>¥n <tr>")
            this_row = row
            html.append(" " + value)
        html.append("  </tr>\n</table></form></body></html>")
        return "\n".join(html)

    def add_title(self, title: str) -> None:
        super().add_title(escape(title))

    def add_label(self, text: str, row: int, column: int, **kwargs) -> None:
        self.items[(row, column)] = ('<td><label for ="{}">{}:</label></td>'.format(kwargs["target"], escape(text)))

    def add_entry(self, variable: str, row: int, column: int, **kwargs) -> None:
        html = """<td><input name="{}" type="{}" /></td>""".format(variable, kwargs.get("kind", "text"))
        self.items[(row, column)] = html

    def add_button(self, text: str, row: int, column) -> None:
        html = """<td><input type="submit" value="{}" /></td>""".format(escape(text))
        self.items[(row, column)] = html
