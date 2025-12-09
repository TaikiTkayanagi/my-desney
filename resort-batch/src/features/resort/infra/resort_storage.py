
from abc import ABCMeta, abstractmethod

from src.features.resort.modeles.real_time_entity import GrJson, Greeting, Restaurant


class ResotrStorage(metaclass=ABCMeta):
    @abstractmethod
    def is_exist_gr_json(self) -> bool:
        pass
    
    @abstractmethod
    def get_gr_names(self) -> tuple[Greeting | None , Restaurant | None]:
        pass

    @abstractmethod
    def save_gr_json(self, register: GrJson) -> None:
        pass