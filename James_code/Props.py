class Props:
    def __init__(self, orientation='N', health=1, velocity=0):
        self.velocity = velocity
        self.orientation = orientation
        self.health = health
        self.mana = 1


class Wizard(Props):
    def __init__(self, orientation, velocity=0):
        Props.__init__(self, orientation, 100, velocity)
        self.mana = 100
        self.said = []

    def shout(self, string):
        self.said.append(string)

    def return_speech(self):
        speech = self.said
        self.said = []
        return speech


class Boulder(Props):
    def __init__(self, orientation, health, velocity=0):
        Props.__init__(self, orientation, health, velocity)
