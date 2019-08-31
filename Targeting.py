class Target:
    def __init__(self, starting_position):
        self.starting_position = starting_position
        self.orientation = None
        self.base_cost = None
        self.level = None

    def cost(self):
        return self.base_cost * self.level

    def properties(self):
        return


class Self(Target):
    def __init__(self, starting_position):
        Target.__init__(self, starting_position)
        self.base_cost = 1

    def properties(self):
        velocity = 0
        return self.starting_position, velocity


class Point(Target):
    def __init__(self, starting_position):
        Target.__init__(self, starting_position)
        self.base_cost = 1

    def properties(self):
        velocity = self.level
        return self.starting_position, velocity
