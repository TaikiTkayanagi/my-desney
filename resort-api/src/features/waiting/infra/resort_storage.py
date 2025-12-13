
from abc import ABCMeta, abstractmethod

from src.features.waiting.models.last_update import LastUpdate


class ResortStorage(metaclass=ABCMeta):
    @abstractmethod
    def get_last_update(self) -> LastUpdate:
        pass 