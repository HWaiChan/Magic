from Elements import *
from Props import *


class SpellEffect:
    def __init__(self, level, action_type):
        self.type = None
        self.setting_type = None
        self.action_type = action_type
        self.base_cost = None
        self.start = None
        self.level = level
        self.velocity = 0

    def cost(self):
        return
    
    def act(self, elements, props):
        if self.action_type == 'Create':
            try:
                elements.append(self.create_element())
            except:
                props.append(self.create_prop())
        return elements, props


class SpellEffectFire(SpellEffect):
    def __init__(self, level, action_type):
        SpellEffect.__init__(self, level, action_type)
        self.type = 'Fire'
        self.setting_type = 'Temperature'
        self.base_cost = 1

    def create_element(self):
        temperature = 400 + (100 * self.level)
        return Fire(temperature)


class SpellEffectCold(SpellEffect):
    def __init__(self, level, action_type):
        SpellEffect.__init__(self, level, action_type)
        self.type = 'Cold'
        self.setting_type = 'Temperature'
        self.base_cost = 1

    def create_element(self):
        temperature = 0 - (25 * self.level)
        return Water(temperature)


class SpellEffectLightning(SpellEffect):
    def __init__(self, level, action_type):
        SpellEffect.__init__(self, level, action_type)
        self.type = 'Lightning'
        self.setting_type = 'Power'
        self.base_cost = 1

    def create_element(self):
        power = (100 * self.level)
        return Lightning(power)


class SpellEffectEarth(SpellEffect):
    def __init__(self, level, action_type):
        SpellEffect.__init__(self, level, action_type)
        self.type = 'Earth'
        self.setting_type = 'Weight'
        self.base_cost = 1

    def create_prop(self):
        health = self.level * 50
        return Boulder(health)


class SpellEffectTime(SpellEffect):
    def __init__(self, level, action_type):
        SpellEffect.__init__(self, level, action_type)
        self.type = 'time'
        self.setting_type = 'Rate'
        self.base_cost = 10
