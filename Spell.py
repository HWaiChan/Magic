class Spell:
    def __init__(self, effect, shape, target, mana, concentration, repeat, spell_code):
        self.spell_effect = effect  # Tile-wide effect
        self.shape = shape
        self.target = target
        self.mana = mana
        self.concentration = concentration
        self.repeat = repeat
        self.code = spell_code
        self.delayed_spell_link = None

    def castable(self):
        return self.target.cost() * self.spell_effect.cost() < int(self.mana)

