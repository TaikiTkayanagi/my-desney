from dataclasses import dataclass

class RealTimes:
    def __init__(self, real_times: list[RealTime]):
        self.list = real_times
    
    def convert_for_register(self, greeting: Greeting, restaurant: Restaurant) -> list[RegisterRealTime]:
        result = []
        for real_time in self.list:
            if real_time.name in greeting.names:
                result.append(RegisterRealTime(
                    area=real_time.area,
                    name=real_time.name,
                    condition=real_time.condition,
                    note=real_time.note,
                    type="greeting"
                ))
            elif real_time.name in restaurant.names:
                result.append(RegisterRealTime(
                    area=real_time.area,
                    name=real_time.name,
                    condition=real_time.condition,
                    note=real_time.note,
                    type="restaurant"
                ))
            else:
                result.append(RegisterRealTime(
                    area=real_time.area,
                    name=real_time.name,
                    condition=real_time.condition,
                    note=real_time.note,
                    type="attraction"
                ))
        return result

@dataclass
class RealTime:
    area: str
    name: str
    condition: str
    note: str | None

@dataclass
class Greeting:
    names: list[str]

@dataclass
class Restaurant:
    names: list[str]
    
@dataclass
class RegisterRealTime(RealTime):
    type: str