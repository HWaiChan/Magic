from Props import Props
import pytest


@pytest.mark.parametrize("velocity, moveable",
                         [((1, 0), True),
                          ((-1, 0), True),
                          ((0, 1), True),
                          ((0, -1), True),
                          ((0, 0), False), ])
def test_prop_want_to_move(velocity, moveable):
    prop = Props(0, (0, 0))
    prop.velocity = velocity
    assert prop.want_to_move() == moveable


@pytest.mark.parametrize("state_temperature, expected_prop_hp",
                         [(1000, 31),
                          (200, 47),
                          (50, 50),
                          (-200, 42),
                          (-50, 48),
                          (0, 50), ])
def test_interact_from_state_temperature(state_temperature, expected_prop_hp):
    dummy_state = {"Temperature": state_temperature, "Rate_of_Time": 1, "Force": (0, 0), "Voltage": 0,
                   "Fuel": False,
                   "Conductor": False}
    prop = Props(orientation=0, health=50, velocity=(0, 0))
    prop.interact_from(dummy_state)
    assert prop.health == expected_prop_hp
