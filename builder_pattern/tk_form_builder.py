import re
from builder_pattern.abstract_form_builder import AbstractFormBuilder


class TkFormBuilder(AbstractFormBuilder):
    TEMPLATE = """#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk

class {name}Form(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)
        self.withdraw()     # hide until ready to show
        self.title("{title}")
        {statements}
        self.bind("<Escape>", lambda *args: self.destroy())
        self.deiconify()    # show when widgets are created and laid out
        if self.winfo_viewable():
            self.transient(master)
        self.wait_visibility()
        self.grab_set()
        self.wait_window(self)

if __name__ == "__main__":
    application = tk.Tk()
    window = {name}Form(application)
    application.protocol("WM_DELETE_WINDOW", application.quit)
    application.mainloop()
"""

    def __init__(self):
        self.title = "TkFormBuilder"
        self.statements = []

    def add_title(self, title: str) -> None:
        super().add_title(title)

    def add_label(self, text: str, row: int, column: int, **kwargs) -> None:
        name = self._canonicalize(text)
        create = """self.{}Label = ttk.Label(self, text="{}:")""".format(
            name, text)
        layout = """self.{}Label.grid(row={}, column={}, sticky=tk.W, padx="0.75m", pady="0.75m")""".format(
            name, row, column)
        self.statements.extend((create, layout))

    def add_entry(self, variable: str, row: int, column: int, **kwargs) -> None:
        name = self._canonicalize(variable)
        extra = "" if kwargs.get("kind") != "password" else ', show="*"'
        create = "self.{}Entry = ttk.Entry(self{})".format(name, extra)
        layout = """self.{}Entry.grid(row={}, column={}, sticky=(tk.W, tk.E), padx="0.75m", pady="0.75m")""".format(
            name, row, column)
        self.statements.extend((create, layout))

    def add_button(self, text: str, row: int, column: int, **kwargs) -> None:
        name = self._canonicalize(text)
        create = ("""self.{}Button = ttk.Button(self, text="{}")"""
                  .format(name, text))
        layout = """self.{}Button.grid(row={}, column={}, padx="0.75m", pady="0.75m")""".format(name, row, column)
        self.statements.extend((create, layout))

    def form(self) -> str:
        return TkFormBuilder.TEMPLATE.format(title=self.title,
                                             name=self._canonicalize(self.title, False),
                                             statements="\n        ".join(self.statements))

    def _canonicalize(self, text: str, startLower=True) -> str:
        text = re.sub(r"\W+", "", text)
        if text[0].isdigit():
            return "_" + text
        return text if not startLower else text[0].lower() + text[1:]
