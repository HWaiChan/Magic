from math import pi, cos, sin

class Elements:
    def __init__(self, velocity=(0, 0)):
        self.velocity = velocity

    def interact_on(self, state):
        return state

    def interact_from(self, state):
        pass


class Fire(Elements):
    def __init__(self, temperature, velocity=(0, 0)):
        Elements.__init__(self, velocity)
        self.temperature = temperature
        self.remaining_duration = 2

    def interact_on(self, state):
        state["Temperature"] = (state["Temperature"] + self.temperature) / 2
        return state

    def interact_from(self, state):
        self.temperature = state["Temperature"]
        self.remaining_duration -= 1
        return self.check_status(state)

    def check_status(self, state):
        if self.temperature > 300 and (state['Fuel'] or self.remaining_duration > 0):
            return self
        else:
            return None


class Water(Elements):
    def __init__(self, temperature, velocity=(0, 0)):
        Elements.__init__(self, velocity)
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

    def interact_from(self, state):
        self.temperature = state["Temperature"]
        return self.check_status(state)

    def check_status(self, state):
        if self.temperature < 0:
            return Ice(self.temperature, self.velocity)
        elif self.temperature > 100:
            return Steam(self.temperature, self.velocity)
        else:
            return self


class Ice(Water):
    def __init__(self, temperature, velocity=(0, 0)):
        Water.__init__(self, temperature, velocity)

    def interact_on(self, state):
        if (state["Temperature"] + self.temperature)/2 < state["Temperature"]:
            state["Temperature"] = (state["Temperature"] + (self.temperature*4.5)/2)
        else:
            state["Temperature"] = (state["Temperature"] + self.temperature)/2

        if state["Temperature"] < -273:
            state["Temperature"] = -273

        return state

    def check_status(self, state):
        if self.temperature < 0:
            return self
        elif self.temperature > 100:
            return Steam(self.temperature, self.position, self.velocity, self.shape)
        else:
            return Water(self.temperature, self.position, self.velocity, self.shape)


class Steam(Water):
    def __init__(self, temperature, velocity=(0, 0)):
        Water.__init__(self, temperature, velocity)

    def check_status(self, state):
        if self.temperature < 0:
            return Ice(self.temperature, self.position, self.velocity, self.shape)
        elif self.temperature > 100:
            return self
        else:
            return Water(self.temperature, self.position, self.velocity, self.shape)


class Lightning(Elements):
    def __init__(self, power, velocity=(0, 0)):
        Elements.__init__(self, velocity)
        self.power = power
        self.remaining_duration = 2

    def interact_on(self, state):
        state["Voltage"] = self.power * 10
        return state

    def interact_from(self, state):
        self.remaining_duration -= 1
        return self.check_status(state)

    def check_status(self, state):
        if state['Conductor'] or self.remaining_duration > 0:
            return self
        else:
            return None


class Force(Elements):
    def __init__(self, power, velocity=(0, 0)):
        Elements.__init__(self, velocity)
        self.power = power
        self.remaining_duration = 2

    def interact_on(self, state):
        state["Force"] = self.power
        return state

    def interact_from(self, state):
        self.remaining_duration -= 1
        return self.check_status(state)

    def check_status(self, state):
        if self.remaining_duration > 0:
            return self
