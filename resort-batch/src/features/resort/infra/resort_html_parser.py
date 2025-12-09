from abc import ABCMeta, abstractmethod

from src.features.resort.modeles.real_time_entity import Greeting, RealTimes, Restaurant


class ResortHtmlParser(metaclass=ABCMeta):
    @abstractmethod
    def pick_up_real_time(self) -> RealTimes:
        pass

    @abstractmethod
    def pick_up_greeting(self) -> Greeting:
        pass

    @abstractmethod
    def pick_up_restrant(self) -> Restaurant:
        pass

class ResortHtmlParserFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_parser(self, html: str) -> ResortHtmlParser:
        pass
