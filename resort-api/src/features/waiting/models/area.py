from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Area:
    _LAND_AREA_DICT: ClassVar[dict[str, str]] = {
        "トゥーンタウン": "toon",
        "ファンタジーランド": "fantasy",
        "トゥモローランド": "tommorow",
        "ワールドバザール": "world",
        "ウエスタンランド": "westan",
        "クリッターカントリー": "country",
        "アドベンチャーランド": "adventure",
    }
    _SEA_AREA_DICT: ClassVar[dict[str, str]] = {
        "ミステリアスアイランド": "mysterious",
        "マーメイドラグーン": "mermaid",
        "アメリカンウォーターフロント": "america",
        "ファンタジースプリングス": "fantasy",
        "ポートディスカバリー": "port",
        "ロストリバーデルタ": "lost",
        "メディテレーニアンハーバー": "mediterranean",
        "アラビアンコースト": "arabian"
    }
    name: str
    attractions: list[Attraction]

    @staticmethod
    def convert(key, place):
        if place == "land":
            if not key in Area._LAND_AREA_DICT:
                return "" 
            return Area._LAND_AREA_DICT[key]
        else:
            if not key in Area._SEA_AREA_DICT:
                return "" 
            return Area._SEA_AREA_DICT[key]


@dataclass
class Areas:
    date_time: str
    list: list[Area]

    def create_response(self):
        ret = {}
        ret["date_time"] = self.date_time
        for area in self.list:
            ret[area.name] = area.attractions
        
        return ret
            
            
@dataclass
class Attraction:
    name: str
    condition: str
    type: str