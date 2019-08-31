class PhysicalEffect:
    def __init__(self, power):
        self.power = power


class PhysicalEffectPropDamage(PhysicalEffect):
    def __init__(self, power):
        PhysicalEffect.__init__(self, power)

    def act(self, elements, props):
        for prop in props:
            prop.health = prop.health - self.power
        return elements, props
