from Props import *
import inspect


class Tile:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.actions = []
        self.elements = []
        self.props = []
        self.speech_log = []
        self.state = {"Temperature": 24, "Time": 1, "Force": (0, 0), "Voltage": 0, "Fuel": False, "Conductor": False}

    def resolve_tile(self):
        self.action_phase()
        self.elements_phase()
        self.props_phase()

    def speech_phase(self):
        self.speech_log =[]
        for prop in self.props:
            one_person_log = prop.return_speech()
            for speech in one_person_log:
                self.speech_log.append(speech)
        return self.speech_log

    def action_phase(self):
        for action in self.actions:
            self.elements, self.props = action.act(self.elements, self.props)
        for props in self.props:
            self.elements = props.prop_effects(self.elements)
        self.actions = []

    def elements_phase(self):
        self.state['Fuel'] = False
        self.state['Conductor'] = False
        self.state['Voltage'] = 0
        self.state["Force"] = (0, 0)

        for element in self.elements:
            self.state = element.interact_on(self.state)
        for objects_index, element in enumerate(self.elements):
            self.elements[objects_index] = element.interact_from(self.state)

        self.elements = list(filter(None, self.elements))

    def props_phase(self):
        for objects_index, prop in enumerate(self.props):
            self.props[objects_index] = prop.interact_from(self.state)

        self.props = list(filter(None, self.props))

    def move_phase(self):
        props_that_want_to_move = []
        for prop in self.props:
            if prop.want_to_move():
                props_that_want_to_move.append((prop, self.coordinates))
                self.props.remove(prop)
        return props_that_want_to_move

    def add_actions(self, action):
        self.actions.append(action)

    def add_prop(self, prop):
        # Todo remove controlled movement
        self.props.append(prop)

    def get_information(self):
        return str(self.coordinates) + " with world effects " + str(len(self.elements))

    def immediate_action(self, action):
        self.elements, self.props = action.act(self.elements, self.props)
