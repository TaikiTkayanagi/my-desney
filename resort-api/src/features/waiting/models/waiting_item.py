from dataclasses import dataclass

from src.features.waiting.models.area import Area, Areas, Attraction


@dataclass
class WaitingItem:
    place_time: str
    id: str
    area: str
    condition: str
    date_time: str
    name: str
    place: str
    type: str

    def convert_to(self, ohl, thl, tml) -> Attraction:
        return Attraction(
            condition=self.condition,
            name=self.name,
            type=self.type,
            ohl=ohl,
            thl=thl,
            tml=tml 
        )


@dataclass
class WaitingItems:
    list: list[WaitingItem]

    def pick_up_name_condition(self):
        ret = {}
        for item in self.list:
            ret[item.name] = item.condition 
        return ret
        

    def group_by_area(self, thirty_minutes_later: dict[str, str], one_hour_later: dict[str, str], three_hour_later: dict[str, str]):
        memo: dict[str, list[Attraction]] = {}
        date_time = ""
        for item in self.list:
            area = Area.convert(item.area, item.place)
            tml = thirty_minutes_later.get(item.name) 
            ohl = one_hour_later.get(item.name)
            thl = three_hour_later.get(item.name) 
            if area in memo:
                memo[area].append(item.convert_to(tml, ohl, thl))
            else:
                memo[area] = [item.convert_to(tml, ohl, thl)]
            if date_time == "":
                date_time = item.date_time

        ret: list[Area] = []
        for key in memo.keys():
            ret.append(Area(key, memo[key]))
        return Areas(date_time, ret)
