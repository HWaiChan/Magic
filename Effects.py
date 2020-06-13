from math import pi, cos, sin


class Effects:
    def __init__(self, velocity=(0, 0)):
        self.velocity = velocity
        self.coords = None

    def interact_on(self, state):
        return state

    def interact_from(self, state):
        return None


class Heat(Effects):
    def __init__(self, temperature, velocity=(0, 0)):
        Effects.__init__(self, velocity)
        self.temperature = temperature

    def interact_on(self, state):
        state["Temperature"] = (state["Temperature"] + self.temperature) / 2
        return state


class Cold(Effects):
    def __init__(self, temperature, velocity=(0, 0)):
        Effects.__init__(self, velocity)
        self.temperature = temperature

    def interact_on(self, state):
        if (state["Temperature"] + self.temperature)/2 < state["Temperature"]:
            state["Temperature"] = (state["Temperature"] + (self.temperature*4.5)/2)
        else:
            state["Temperature"] = (state["Temperature"] + self.temperature)/2

        if state["Temperature"] < -273:
            state["Temperature"] = -273

        state['Conductor'] = True
        return state


class Conductivity(Effects):
    def __init__(self, velocity=(0, 0)):
        Effects.__init__(self, velocity)

    def interact_on(self, state):
        state['Conductor'] = True
        return state


class Electricity(Effects):
    def __init__(self, power, velocity=(0, 0)):
        Effects.__init__(self, velocity)
        self.power = power

    def interact_on(self, state):
        state["Voltage"] = self.power * 10
        return state


class Force(Effects):
    def __init__(self, power, velocity=(0, 0)):
        Effects.__init__(self, velocity)
        self.power = power

    def interact_on(self, state):
        state["Force"] = self.power
        return state

