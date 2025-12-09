from abc import ABCMeta, abstractmethod

from src.features.resort.modeles.real_time_entity import RegisterRealTime


class WaitingRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, items: list[RegisterRealTime], datetime: str, place: str) -> None:
        pass