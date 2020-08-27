from Props import Wizard
import pytest


@pytest.mark.parametrize("initial_wizard_mana, spell_cost, expect_cast, final_wizard_mana",
                        [(100, 25, True, 75),
                         (25, 25, True, 0),
                         (10, 25, False, 10),
                         (10, 0, True, 10),
                         (0, 0, True, 0)])
def test_shout_spends_mana(initial_wizard_mana, spell_cost, expect_cast, final_wizard_mana):
    wizard = Wizard(0, (0, 0))
    wizard.mana = initial_wizard_mana
    shout_string = 'Mana ' + str(spell_cost)
    wizard.shout(shout_string)
    assert wizard.mana == final_wizard_mana, "Wizard should have expended Mana to cast."
    if expect_cast:
        assert shout_string in wizard.said
    else:
        assert shout_string not in wizard.said
