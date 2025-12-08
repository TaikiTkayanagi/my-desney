from abc import ABCMeta, abstractmethod


class ResortHtmlParser(metaclass=ABCMeta):
    @abstractmethod
    def pick_up_realtimes(self) -> list[dict]:
        pass

class ResortHtmlParserFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_parser(self, html: str) -> ResortHtmlParser:
        pass
