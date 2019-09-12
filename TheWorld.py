from Tile import Tile
from pprint import pprint
import copy
from SpellDecoder import *
from math import pi, cos, sin
import numpy as np
from PhysicalEffects import *
from SpellShapes import *
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


WORLD_SIZE = 10


class TheWorld(metaclass=Singleton):

    def __init__(self):
        print("Starting The world.....")
        self.tiles = [[]]
        self.prepare_tiles()

    def prepare_tiles(self):
        self.tiles = [[Tile([x, y]) for x in range(WORLD_SIZE)] for y in range(WORLD_SIZE)]
        return

    def add_spell(self, spell):
        """
            edits the world grid of tiles based on world element shape and position
        :param spell:
        :param world_action such as a Spell
        :return:
        """
        world_position = spell.target.position
        rotation_angle = spell.shape.orientation * pi / 180

        # TODO: abstract away the rotational matrix logic
        rotational_matrix = [[cos(rotation_angle), -sin(rotation_angle)], [sin(rotation_angle), cos(rotation_angle)]]
        for relative_coords in spell.shape.get_relative_affected_tiles():
            [rotated_y, rotated_x] = np.matmul(relative_coords, rotational_matrix)
            shifted_y = world_position[1] + rotated_y
            shifted_x = world_position[0] + rotated_x
            spell_effect_copy = copy.copy(spell.spell_effect)
            self.tiles[int(round(shifted_y))][int(round(shifted_x))].add_actions(spell_effect_copy)

    def resolve_tiles(self):
        tile_speech_log = []

        for i in self.tiles:
            for j in i:
                tile_speech_log = j.speech_phase()
                for speech in tile_speech_log:
                    if not speech is None:
                        spelldecoder = SpellDecoder(speech)
                        spell = spelldecoder.decode_spell(j.coordinates)
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
            self.tiles[coord[1] - int(prop.velocity[1])][coord[0] - int(prop.velocity[0])].add_prop(prop)
            if prop.velocity[0] == 0:
                rotation_angle = 90
            elif prop.velocity[1] == 0:
                rotation_angle = 0
            else:
                rotation_angle = np.arctan(prop.velocity[0]/prop.velocity[1])
            rotational_matrix = [[cos(rotation_angle), -sin(rotation_angle)],
                                 [sin(rotation_angle), cos(rotation_angle)]]
            line = Line(int(np.hypot(prop.velocity[0], prop.velocity[1])))
            old_shifted_y = 0
            old_shifted_x = 0
            for relative_coords in line.get_relative_affected_tiles():
                [rotated_y, rotated_x] = np.matmul(relative_coords, rotational_matrix)
                shifted_y = int(round(coord[1] - rotated_y))
                shifted_x = int(round(coord[0] + rotated_x))
                if old_shifted_y != shifted_y and shifted_x != old_shifted_x:
                    old_shifted_x = shifted_x
                    old_shifted_y = shifted_y
                    self.tiles[shifted_y][shifted_x].immediate_action(PhysicalEffectPropDamage(int(np.hypot(prop.velocity[0], prop.velocity[1]))*10))

    def print_elements_grid(self):
        pprint([[len(j.elements) for j in i] for i in self.tiles])

    def print_props_grid(self):
        pprint([[len(j.props) for j in i] for i in self.tiles])

    def print_action_grid(self):
        pprint([[len(j.actions) for j in i] for i in self.tiles])

    def get_total_elements(self):
        elements = 0
        for i in self.tiles:
            for j in i:
                elements += len(j.elements)
        return elements

    def get_total_actions(self):
        action = 0
        for i in self.tiles:
            for j in i:
                action += len(j.actions)
        return action
