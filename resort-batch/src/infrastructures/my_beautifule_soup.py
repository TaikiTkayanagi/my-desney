

from bs4 import BeautifulSoup
from src.services.resort_service.resort_html_parser import ResortHtmlParser, ResortHtmlParserFactory


class MyBeautifuleSoup(ResortHtmlParser):
    def __init__(self, html) -> None:
        self.my_parser = BeautifulSoup(html, "html.parser")

    def pick_up_realtimes(self) -> list[dict]:
        realtime_tags = self.my_parser.find_all("div", class_="realtime-attr")
        result = []
        for realtime_tag in realtime_tags:
            name = realtime_tag.find("div", class_="realtime-attr-name")
            time = realtime_tag.find("div", class_="realtime-attr-condition")
            timetable = realtime_tag.find("div", class_="greeting_timetable")

            attraction_info = {}
            if name:
                attraction_info["name"] = name.text
            if time:
                attraction_info["time"] = time.text.strip()
            if timetable:
                attraction_info["timetable"] = timetable.text
            result.append(attraction_info)
        return result


class MyBeautifuleSoupFactory(ResortHtmlParserFactory):
    def create_parser(self, html: str) -> ResortHtmlParser:
        return MyBeautifuleSoup(html)