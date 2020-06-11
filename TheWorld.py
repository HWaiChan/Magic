from Tile import Tile
from pprint import pprint
import copy
from SpellDecoder import *
from math import pi, cos, sin
import numpy as np
from PhysicalEffects import *
from SpellShapes import *
from WorldMaths import WorldMaths


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


WORLD_SIZE = 12


class TheWorld(metaclass=Singleton):

    def __init__(self):
        print("Starting The world.....")
        self.tiles = [[Tile([y, x]) for x in range(WORLD_SIZE)] for y in range(WORLD_SIZE)]

    def add_spell(self, spell):
        """
            Divvys up the spell_effects depending on the spell's shape, orientation and position.
        :param spell:
        :param world_action such as a Spell
        :return:
        """
        true_coords = WorldMaths.get_true_coordinates(spell.target.position, spell.shape.orientation,
                                                      spell.shape.get_relative_affected_tiles())
        for true_c in true_coords:
            spell_effect_copy = copy.copy(spell.spell_effect)
            self.tiles[int(round(true_c[0]))][int(round(true_c[1]))].add_actions(spell_effect_copy)

    def add_prop(self, prop, location):
        self.tiles[location[0]][location[1]].props.append(prop)

    def resolve_tiles(self):
        for i in self.tiles:
            for j in i:
                tile_speech_log = j.speech_phase()
                for speech in tile_speech_log:
                    if speech is not None:
                        spell = SpellDecoder(speech).decode_spell(j.coordinates)
                        if spell.castable():
                            self.add_spell(spell)

        for i in self.tiles:
            for j in i:
                j.resolve_tile()

        props_that_want_to_move = []
        for i in self.tiles:
            for j in i:
                props_that_want_to_move = props_that_want_to_move + j.move_phase()

        for prop, coord in props_that_want_to_move:
            if coord[0] + int(prop.velocity[0]) <= len(self.tiles) - 1 and \
                    coord[1] + int(prop.velocity[1]) <= len(self.tiles[0]) - 1:
                self.tiles[coord[0] + int(prop.velocity[0])][coord[1] + int(prop.velocity[1])].add_prop(prop)
            if prop.velocity[0] == 0:
                rotation_angle = 90
            elif prop.velocity[1] == 0:
                rotation_angle = 0
            else:
                rotation_angle = np.arctan(prop.velocity[0] / prop.velocity[1]) * 180 / pi
            line = Line(int(np.hypot(prop.velocity[0], prop.velocity[1])))
            true_coords = WorldMaths.get_true_coordinates(coord, rotation_angle,
                                                          line.get_relative_affected_tiles())
            for true_c in true_coords:
                if true_c[0] <= len(self.tiles) - 1 and true_c[1] <= len(self.tiles[0]) - 1:
                    self.tiles[true_c[0]][true_c[1]].immediate_action(
                        PhysicalEffectPropDamage(int(np.hypot(prop.velocity[0], prop.velocity[1])) * 10))

    def print_elements_grid(self):
        '''
        Displays the number of elements present in each tile.
        Co-ords are increasing y is UP and increasing x is RIGHT.
        :return:
        '''
        print("Elements")
        pprint([[len(j.effects) for j in i] for i in reversed(self.tiles)])

    def print_props_grid(self):
        '''
        Displays the number of props present in each tile.
        Co-ords are increasing y is UP and increasing x is RIGHT.
        :return:
        '''
        print("Props")
        pprint([[len(j.props) for j in i] for i in reversed(self.tiles)])

    def print_action_grid(self):
        '''
        Displays the number of actions present in each tile.
        Co-ords are increasing y is UP and increasing x is RIGHT.
        :return:
        '''
        print("Action")
        pprint([[len(j.actions) for j in i] for i in reversed(self.tiles)])

    def get_total_elements(self):
        elements = 0
        for i in self.tiles:
            for j in i:
                elements += len(j.effects)
        return elements

    def get_total_actions(self):
        action = 0
        for i in self.tiles:
            for j in i:
                action += len(j.actions)
        return action
