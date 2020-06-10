from math import pi, cos, sin
from Effects import *

class Props:
    def __init__(self, orientation=0, health=1, velocity=(0, 0)):
        self.velocity = velocity
        self.orientation = orientation
        self.health = health
        self.mana = 1
        self.collidable = True

    def want_to_move(self):
        return self.velocity != (0, 0)

    def return_speech(self):
        return []

    def interact_from(self, state):
        if state["Temperature"] > 50:
            self.health = int(self.health - ((state["Temperature"] - 50) / 50))
        elif state["Temperature"] < 0:
            self.health = int(self.health + (state["Temperature"] / 25))
        if state["Voltage"] > 0:
            self.health = int(self.health - (state["Voltage"] / 50))
        if state["Force"] != (0, 0):
            self.velocity = (self.velocity[0] + state["Force"][0], self.velocity[1] + state["Force"][1])

        self.internal_interact()

    def internal_interact(self):
        pass

    def prop_effects(self, effects):
        return effects

class Wizard(Props):
    def __init__(self, orientation, velocity=(0, 0)):
        Props.__init__(self, orientation, 100, velocity)
        self.mana = 100
        self.said = []
        self.controlled_movement = (0, 0)
        self.added_movement = (0, 0)

    def shout(self, string):
        components = string.split()
        if "Mana" in components:
            if self.mana > int(components[components.index("Mana") + 1]):
                self.mana = self.mana - int(components[components.index("Mana") + 1])
                self.said.append(string)

    def return_speech(self):
        speech = self.said
        self.said = []
        return speech

    def movement(self, velocity):
        self.controlled_movement = velocity

    def internal_interact(self):
        self.velocity = (self.velocity[0] - self.added_movement[0], self.velocity[1] - self.added_movement[1])
        self.velocity = (self.velocity[0] + self.controlled_movement[0], self.velocity[1] + self.controlled_movement[1])
        self.added_movement = self.controlled_movement
        self.controlled_movement = (0, 0)


class Boulder(Props):
    def __init__(self, orientation, health, velocity=(0, 0)):
        Props.__init__(self, orientation, health, velocity)


class Fire(Props):
    def __init__(self,  temperature, orientation=0, health=1, velocity=(0, 0)):
        Props.__init__(self, orientation, health, velocity)
        self.collidable = False
        self.remaining_duration = 2
        self.temperature = temperature

    def interact_from(self, state):

        self.temperature = state["Temperature"]
        self.remaining_duration -= 1
        if self.temperature > 300 and (state['Fuel'] or self.remaining_duration > 0):
            self.health = 0

    def prop_effects(self, effects):
        if self.health > 0:
            effects.add(Heat(self.temperature))
        return effects
