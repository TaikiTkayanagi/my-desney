

from src.features.resort.modeles.real_time_entity import Greeting, RealTime, RealTimes, RegisterRealTime, Restaurant


def test_convert_for_register():
    sut = RealTimes([
        RealTime(area="Area1", name="Greet1", condition="Open", note="Note1"),
        RealTime(area="Area2", name="Rest1", condition="Closed", note=None),
        RealTime(area="Area3", name="Attr1", condition="Operating", note="Note3"),
    ])
    greeting = Greeting(names=["Greet1", "Greet2"])
    restaurant = Restaurant(names=["Rest1", "Rest2"])

    result = sut.convert_for_register(greeting, restaurant)

    assert result[0] == RegisterRealTime(area="Area1", name="Greet1", condition="Open", note="Note1", type="greeting")
    assert result[1] == RegisterRealTime(area="Area2", name="Rest1", condition="Closed", note=None, type="restaurant") 
    assert result[2] == RegisterRealTime(area="Area3", name="Attr1", condition="Operating", note="Note3", type="attraction")