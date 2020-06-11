class Spell:
    def __init__(self, effect, shape, target, mana, concentration):
        self.spell_effect = effect  # Tile-wide effect
        self.shape = shape
        self.target = target
        self.mana = mana
        self.concentration = concentration

    def castable(self):
        return self.target.cost() * self.spell_effect.cost() < int(self.mana)

