from abc import ABCMeta, abstractmethod

from src.features.resort.modeles.date_time import MyDateTime
from src.features.resort.modeles.real_time_entity import RegisterRealTime


class WaitingRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, items: list[RegisterRealTime], datetime: MyDateTime, place: str) -> None:
        pass