
from abc import ABCMeta, abstractmethod

from src.features.resort.modeles.date_time import MyDateTime
from src.features.resort.modeles.real_time_entity import GrJson, Greeting, Restaurant


class ResotrStorage(metaclass=ABCMeta):
    @abstractmethod
    def is_exist_gr_json(self, gr_json_key: str) -> bool:
        pass
    
    @abstractmethod
    def get_gr_names(self, gr_json_key: str) -> tuple[Greeting | None , Restaurant | None]:
        pass

    @abstractmethod
    def save_gr_json(self,gr_json_key, register: GrJson) -> None:
        pass

    @abstractmethod
    def save_place_time_if_not_cache(self, body: bytes) -> None:
        pass