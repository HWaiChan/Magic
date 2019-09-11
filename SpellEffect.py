from Elements import *
from Props import *
from math import pi, cos, sin

class SpellEffect:
    def __init__(self, level, action_type, orientation=0):
        self.type = None
        self.setting_type = None
        self.action_type = action_type
        self.base_cost = None
        self.start = None
        self.level = level
        self.velocity = 0
        self.orientation = orientation

    def cost(self):
        return int(self.base_cost) + int(self.level)
    
    def act(self, elements, props):
        if self.action_type == 'Create':
            try:
                elements.append(self.create_element())
            except:
                props.append(self.create_prop())
        elif self.action_type == 'Destroy':
            try:
                self.destroy_elements(elements)
            except:
                self.destroy_props(props)
        elif self.action_type == 'Displace':
            try:
                self.displace_elements(elements)
            except:
                self.displace_props(props)
        return elements, props


class SpellEffectFire(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, orientation)
        self.type = 'Fire'
        self.setting_type = 'Temperature'
        self.base_cost = 1

    def create_element(self):
        temperature = 400 + (100 * self.level)
        return Fire(temperature)


class SpellEffectCold(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, orientation)
        self.type = 'Cold'
        self.setting_type = 'Temperature'
        self.base_cost = 1

    def create_element(self):
        temperature = 0 - (25 * self.level)
        return Water(temperature)


class SpellEffectLightning(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, orientation)
        self.type = 'Lightning'
        self.setting_type = 'Power'
        self.base_cost = 1

    def create_element(self):
        power = (100 * self.level)
        return Lightning(power)


class SpellEffectEarth(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, float(orientation))
        self.type = 'Earth'
        self.setting_type = 'Weight'
        self.base_cost = 1

    def create_prop(self):
        health = self.level * 50
        return Boulder(self.orientation, health)

    def destroy_props(self, props):
        for prop in props:
            if isinstance(prop, Boulder):
                if self.level * 50 >= prop.health:
                    props.remove(prop)
        return props

    def displace_props(self, props):
        for prop in props:
            if isinstance(prop, Boulder):
                rotation_angle = self.orientation * pi / 180
                prop.velocity = (prop.velocity[0] + self.level * sin(rotation_angle),
                                 prop.velocity[1] + self.level * cos(rotation_angle))

        return props


class SpellEffectTime(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, orientation)
        self.type = 'time'
        self.setting_type = 'Rate'
        self.base_cost = 10
