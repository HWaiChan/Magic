from math import pi, cos, sin

class Props:
    def __init__(self, orientation=0, health=1, velocity=(0, 0)):
        self.velocity = velocity
        self.orientation = orientation
        self.health = health
        self.mana = 1

    def want_to_move(self):
        return self.velocity != (0, 0)

    def return_speech(self):
        return []

    def interact_from(self, state):
        if state["Temperature"] > 50:
            self.health = self.health - ((state["Temperature"] - 50) / 50)
        elif state["Temperature"] < 0:
            self.health = self.health + (state["Temperature"] / 25)
        if state["Voltage"] > 0:
            self.health = self.health - (state["Voltage"] / 50)


class Wizard(Props):
    def __init__(self, orientation, velocity=(0, 0)):
        Props.__init__(self, orientation, 100, velocity)
        self.mana = 100
        self.said = []

    def shout(self, string):
        self.said.append(string)

    def return_speech(self):
        speech = self.said
        self.said = []
        return speech

    # Todo Wizaards need momvment commands


class Boulder(Props):
    def __init__(self, orientation, health, velocity=(0, 0)):
        Props.__init__(self, orientation, health, velocity)
