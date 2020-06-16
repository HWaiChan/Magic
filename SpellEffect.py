from Effects import *
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
        self.linked_caster = None
        self.created_props = []

    def cost(self):
        return int(self.base_cost) + int(self.level)
    
    def act(self, elements, props):
        if self.action_type == 'Create':
            self.create(props, elements)

        elif self.action_type == 'Destroy':
            self.destroy(props, elements)

        elif self.action_type == 'Displace':
            self.displace(props, elements)

        return elements, props


class SpellEffectFire(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, float(orientation))
        self.type = 'Fire'
        self.setting_type = 'Temperature'
        self.base_cost = 1

    def create(self, props, elements):
        temperature = 400 + (100 * self.level)

        props.append(Fire(temperature))
        self.created_props.append(props[-1])
        if self.linked_caster is not None:
            self.linked_caster.concentrated_effects_and_props.append(props[-1])
        return props, elements

    def displace(self, props, elements):
        for prop in props:
            if isinstance(prop, Fire):
                rotation_angle = self.orientation * pi / 180
                prop.velocity = (prop.velocity[0] + self.level * cos(rotation_angle),
                                 prop.velocity[1] + self.level * sin(rotation_angle))

        return props, elements


class SpellEffectCold(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, orientation)
        self.type = 'Cold'
        self.setting_type = 'Temperature'
        self.base_cost = 1

    def create(self, props, elements):
        temperature = 0 - (25 * self.level)
        props.append(Water(temperature))
        self.created_props.append(props[-1])
        if self.linked_caster is not None:
            self.linked_caster.concentrated_effects_and_props.append(props[-1])
        return props, elements


class SpellEffectLightning(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, orientation)
        self.type = 'Lightning'
        self.setting_type = 'Power'
        self.base_cost = 1

    def create(self, props, elements):
        power = (100 * self.level)
        props.append(Lightning(power))
        self.created_props.append(props[-1])
        if self.linked_caster is not None:
            self.linked_caster.concentrated_effects_and_props.append(props[-1])
        return props, elements


class SpellEffectEarth(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, float(orientation))
        self.type = 'Earth'
        self.setting_type = 'Weight'
        self.base_cost = 1

    def create(self, props, elements):
        health = self.level * 50
        props.append(Boulder(self.orientation, health))
        self.created_props.append(props[-1])
        if self.linked_caster is not None:
            self.linked_caster.concentrated_effects_and_props.append(props[-1])
        return props, elements

    def destroy(self, props, elements):
        for prop in props:
            if isinstance(prop, Boulder):
                if self.level * 50 >= prop.health:
                    props.remove(prop)
        return props, elements

    def displace(self, props, elements):
        for prop in props:
            if isinstance(prop, Boulder):
                rotation_angle = self.orientation * pi / 180
                prop.velocity = (prop.velocity[0] + self.level * cos(rotation_angle),
                                 prop.velocity[1] + self.level * sin(rotation_angle))

        return props, elements


class SpellEffectForce(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, float(orientation))
        self.type = 'Earth'
        self.setting_type = 'Weight'
        self.base_cost = 1

    def create(self, props, elements):
        power = (self.level, 0)
        elements.append(Force(power))
        if self.linked_caster is not None:
            self.linked_caster.concentrated_effects_and_props.append(elements[-1])
        return props, elements


class SpellEffectTime(SpellEffect):
    def __init__(self, level, action_type, orientation=0):
        SpellEffect.__init__(self, level, action_type, orientation)
        self.type = 'time'
        self.setting_type = 'Rate'
        self.base_cost = 10
