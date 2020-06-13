from Props import *
import inspect


class Tile:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.actions = []
        self.effects = []
        self.props = []
        self.speech_log = {}
        self.state = {"Temperature": 24, "Time": 1, "Force": (0, 0), "Voltage": 0, "Fuel": False, "Conductor": False}

    def resolve_tile(self):
        self.action_phase()
        self.effects_phase()
        self.props_phase()

    def speech_phase(self):
        self.speech_log = {}
        for prop in self.props:
            one_person_log = prop.return_speech()
            self.speech_log[prop] = []
            for speech in one_person_log:
                self.speech_log[prop].append(speech)
        return self.speech_log

    def action_phase(self):
        for action in self.actions:
            self.effects, self.props = action.act(self.effects, self.props)
        for props in self.props:
            self.effects = props.prop_effects(self.effects)
        self.actions = []

    def effects_phase(self):
        self.state['Fuel'] = False
        self.state['Conductor'] = False
        self.state['Voltage'] = 0
        self.state["Force"] = (0, 0)

        for element in self.effects:
            self.state = element.interact_on(self.state)
        for objects_index, element in enumerate(self.effects):
            self.effects[objects_index] = element.interact_from(self.state)

        self.effects = list(filter(None, self.effects))

        # This is silly
        for effect in self.effects:
            effect.coords = self.coordinates

    def props_phase(self):
        for objects_index, prop in enumerate(self.props):
            self.props[objects_index] = prop.interact_from(self.state)

        self.props = list(filter(None, self.props))

        # This is silly
        for prop in self.props:
            prop.coords = self.coordinates

    def move_phase(self):
        props_that_want_to_move = []
        for prop in self.props:
            if prop.want_to_move():
                props_that_want_to_move.append((prop, self.coordinates))
                self.props.remove(prop)
        return props_that_want_to_move

    def add_actions(self, action):
        self.actions.append(action)

    def add_prop_to_tile(self, prop):
        # Todo remove controlled movement
        prop.coords = self.coordinates
        self.props.append(prop)

    def get_information(self):
        return str(self.coordinates) + " with world effects " + str(len(self.effects))

    def immediate_action(self, action):
        self.effects, self.props = action.act(self.effects, self.props)
