

from src.features.resort.modeles.real_time_entity import Greeting, RealTime, RealTimes, RegisterRealTime, Restaurant


def test_convert_for_register():
    sut = RealTimes([
        RealTime(area="Area1", name="Greet1", condition="Open"),
        RealTime(area="Area2", name="Rest1", condition="Closed"),
        RealTime(area="Area3", name="Attr1", condition="Operating"),
    ])
    greeting = Greeting(names=["Greet1", "Greet2"])
    restaurant = Restaurant(names=["Rest1", "Rest2"])

    result = sut.convert_for_register(greeting, restaurant)

    assert result[0] == RegisterRealTime(area="Area1", name="Greet1", condition="Open", type="greeting")
    assert result[1] == RegisterRealTime(area="Area2", name="Rest1", condition="Closed", type="restaurant") 
    assert result[2] == RegisterRealTime(area="Area3", name="Attr1", condition="Operating", type="attraction")