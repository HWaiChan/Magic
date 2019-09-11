class Target:
    def __init__(self, position):
        self.position = position
        self.orientation = None
        self.base_cost = None
        self.level = None

    def cost(self):
        return self.base_cost + self.level


class Self(Target):
    def __init__(self, position):
        Target.__init__(self, position)
        self.base_cost = 1
        self.level = 0


class Point(Target):
    def __init__(self, starting_position, coordinates=(0, 0)):
        Target.__init__(self, starting_position)
        self.base_cost = 1
        self.level = abs(int(coordinates[0])) + abs(int(coordinates[1]))
        self.position = (starting_position[0] - int(coordinates[0]), starting_position[1] - int(coordinates[1]))