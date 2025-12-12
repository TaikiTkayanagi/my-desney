from dataclasses import dataclass


@dataclass
class ResortPlace:
    _LAND_KEY = "gr_json/land_gr_json.json"
    _SEA_KEY = "gr_json/sea_gr_json.json"
    value: str

    def get_gr_key(self):
        return self._LAND_KEY if self.value == "land" else self._SEA_KEY 
    