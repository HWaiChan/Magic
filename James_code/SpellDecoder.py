from Targeting import *
from Spell import *
from SpellShapes import *
from SpellEffect import *


class SpellDecoder:
    def __init__(self, incantation):
        self.incantation = incantation
        self.spell_effects_dict = {'Fire': lambda string_num, action_string: SpellEffectFire(int(string_num), action_string),
                                   'Cold': lambda string_num, action_string: SpellEffectCold(int(string_num), action_string),
                                   'Lightning': lambda string_num, action_string: SpellEffectLightning(int(string_num), action_string),
                                   'Earth': lambda string_num, action_string: SpellEffectEarth(int(string_num), action_string)}
        self.action_list = ['Create', 'Destroy', 'Displace']
        self.shapes_dict = {'Square': lambda string_num: Square(int(string_num)),
                            'Rectangle': lambda string_num: Rectangle(int(string_num))}
        self.targeting_dict = {'Point': lambda position: Point(position),
                               'Self': lambda position: Self(position)}

    def decode_spell(self, position):
        spell_components = self.incantation.split()
        action = None
        for possible_action in self.action_list:
            if possible_action in spell_components:
                action = possible_action

        for key in self.spell_effects_dict.keys():
            if key in spell_components:
                effect_index = spell_components.index(key)
                effect = self.spell_effects_dict[spell_components[effect_index]](spell_components[effect_index + 1], spell_components[spell_components.index(action)])

        for key in self.shapes_dict.keys():
            if key in spell_components:
                shape_index = spell_components.index(key)
                shape = self.shapes_dict[spell_components[shape_index]](spell_components[shape_index + 1])

        for key in self.targeting_dict.keys():
            if key in spell_components:
                targeting_index = spell_components.index(key)
                target = self.targeting_dict[spell_components[targeting_index]](position)

        return Spell(effect, shape, target)

