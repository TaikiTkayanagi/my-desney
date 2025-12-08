from abc import ABCMeta, abstractmethod


class ResortRequests(metaclass=ABCMeta):
    @abstractmethod
    def fetch_html_text(self, url: str) -> str:
        pass
        