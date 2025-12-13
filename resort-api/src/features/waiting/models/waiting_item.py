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

    def convert_to(self) -> Attraction:
        return Attraction(
            condition=self.condition,
            name=self.name,
            type=self.type
        )


@dataclass
class WaitingItems:
    list: list[WaitingItem]

    def group_by_area(self):
        memo: dict[str, list[Attraction]] = {}
        date_time = ""
        for item in self.list:
            area = Area.convert(item.area, item.place)
            if area in memo:
                memo[area].append(item.convert_to())
            else:
                memo[area] = [item.convert_to()]
            if date_time == "":
                date_time = item.date_time

        ret: list[Area] = []
        for key in memo.keys():
            ret.append(Area(key, memo[key]))
        return Areas(date_time, ret)
