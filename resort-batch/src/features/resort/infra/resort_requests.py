from abc import ABCMeta, abstractmethod

from src.features.resort.modeles.real_time_entity import Greeting, RealTimes, Restaurant



class ResortRequests(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self, url: str) -> str:
        pass

        