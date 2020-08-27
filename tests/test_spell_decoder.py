from SpellDecoder import SpellDecoder
import pytest


@pytest.mark.parametrize("element",
                         ['Fire',
                          'Cold',
                          'Lightning',
                          'Earth', ])
def test_spell_create_element(element):
    incantation = element + ' 3 Create Square 1 Point -1 -1 Mana 25'
    position = (0, 0)
    decoder = SpellDecoder(incantation)
    spells = decoder.decode_spell(position)
    first_spell = spells[0]
    assert first_spell.spell_effect.type == element
