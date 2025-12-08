from requests import Session
import requests
from src.services.resort_service.resort_requests import ResortRequests


class MyRequests(ResortRequests):
    def __init__(self) -> None:
        self.my_requests: Session = requests.Session() 

    def fetch_html_text(self, url: str) -> str:
        response = self.my_requests.get(url)
        return response.text
