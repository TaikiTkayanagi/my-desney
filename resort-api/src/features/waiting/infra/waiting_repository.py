from abc import ABCMeta, abstractmethod

from src.features.waiting.models.last_update import LastUpdate
from src.features.waiting.models.waiting_item import WaitingItems


class WaitingRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_by(self, last_update: LastUpdate, place: str) -> WaitingItems:
       pass 
    