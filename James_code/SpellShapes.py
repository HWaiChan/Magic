from math import ceil, floor
from abc import ABC, abstractmethod


class SpellShapes(ABC):
    def __init__(self):
        self.base_cost = None
        self.level = None

    @abstractmethod
    def get_relative_affected_tiles(self):
        pass


class Square(SpellShapes):
    def __init__(self, size):
        super()
        self.edge_size = size

    def get_relative_affected_tiles(self):
        affected_tiles = []
        for x in range(self.edge_size):
            for y in range(self.edge_size):
                affected_tiles.append((y - floor(self.edge_size / 2), x - floor(self.edge_size / 2)))
        return affected_tiles


class Rectangle(SpellShapes):
    def __init__(self, size):
        super()
        self.distance = 6
        self.width = 3

    def get_relative_affected_tiles(self):
        affected_tiles = []
        for x in range(self.width):
            for y in range(self.distance):
                affected_tiles.append((y - floor(self.distance / 2), x - floor(self.width / 2)))
        return affected_tiles
