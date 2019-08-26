from Tile import Tile
from pprint import pprint
import copy
from SpellDecoder import *


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
        :param world_action such as a Spell
        :return:
        """
        world_position = spell.target.starting_position
        for tile_coords in spell.shape.get_relative_affected_tiles():
            y = world_position[1] + tile_coords[0]
            x = world_position[0] + tile_coords[1]
            spell_effect_copy = copy.copy(spell.spell_effect)
            self.tiles[y][x].add_actions(spell_effect_copy)

    def resolve_tiles(self):
        tile_speech_log = []
        for i in self.tiles:
            for j in i:
                tile_speech_log = j.speech_phase()
                for speech in tile_speech_log:
                    if not speech is None:
                        spelldecoder = SpellDecoder(speech)
                        spell = spelldecoder.decode_spell(j.coordinates)
                        self.add_spell(spell)

        for i in self.tiles:
            for j in i:
                j.resolve_tile()

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
