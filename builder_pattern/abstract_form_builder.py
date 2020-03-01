from abc import ABCMeta, abstractmethod


class AbstractFormBuilder(metaclass=ABCMeta):
    @abstractmethod
    def add_title(self, title) -> None:
        self.title = title

    @abstractmethod
    def form(self) -> str:
        pass

    @abstractmethod
    def add_label(self, text: str, row: int, column: int, **kwargs) -> None:
        pass

    @abstractmethod
    def add_entry(self, variable: str, row: int, column: int, **kwargs) -> None:
        pass

    @abstractmethod
    def add_button(self, text: str, row: int, column) -> None:
        pass
