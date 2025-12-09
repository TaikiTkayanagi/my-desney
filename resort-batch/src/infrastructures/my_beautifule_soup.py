from bs4 import BeautifulSoup, Tag
from src.features.resort.infra.resort_html_parser import ResortHtmlParser, ResortHtmlParserFactory
from src.features.resort.modeles.real_time_entity import Greeting, RealTime, RealTimes, Restaurant

class CLASSNAME:
    REALTIME_ATTR = "realtime-attr"
    AREA_NAME = "area_name"
    REALTIME_NAME = "realtime-attr-name"
    REALTIME_CONDITION = "realtime-attr-condition"
    GREETING_TIMETABLE = "greeting_timetable"

class MyBeautifuleSoup(ResortHtmlParser):
    
    def __init__(self, html) -> None:
        self.my_parser = BeautifulSoup(html, "html.parser")

    def pick_up_real_time(self) -> RealTimes:
        real_time_tags = self._find_all_by_div(self.my_parser, CLASSNAME.REALTIME_ATTR)
        result = []
        for parent in real_time_tags:
            area_tag = self._find_previous_by_h3(parent, CLASSNAME.AREA_NAME)
            name_tag = self._find_by_div(parent, CLASSNAME.REALTIME_NAME)
            condition_tag = self._find_by_div(parent, CLASSNAME.REALTIME_CONDITION)
            note_tag = self._find_by_div(parent, CLASSNAME.GREETING_TIMETABLE)

            area = area_tag.text.strip() if area_tag else ""
            name = name_tag.text.strip() if name_tag else ""
            condition = condition_tag.text.strip() if condition_tag else ""
            note = note_tag.text.strip() if note_tag else None
            result.append(RealTime(
                area=area,
                name=name,
                condition=condition,
            ))
        return RealTimes(result)
    
    def pick_up_greeting(self) -> Greeting:
        name_tags = self._find_all_by_div(self.my_parser, CLASSNAME.REALTIME_NAME)
        result = []
        for name_tag in name_tags:
            name = name_tag.text.strip() if name_tag else ""
            result.append(name)
        return Greeting(names=result)


    def pick_up_restrant(self) -> Restaurant:
        name_tags = self._find_all_by_div(self.my_parser, CLASSNAME.REALTIME_NAME)
        result = []
        for name_tag in name_tags:
            name = name_tag.text.strip() if name_tag else ""
            result.append(name)
        return Restaurant(names=result)

    def _find_all_by_div(self, parent: Tag, class_name: str):
        return parent.find_all("div", class_=class_name)

    def _find_by_div(self, parent: Tag, class_name: str):
        return parent.find("div", class_=class_name)

    def _find_previous_by_h3(self, parent: Tag, class_name: str):
        return parent.find_previous("h3", class_=class_name)


class MyBeautifuleSoupFactory(ResortHtmlParserFactory):
    def create_parser(self, html: str) -> ResortHtmlParser:
        return MyBeautifuleSoup(html)