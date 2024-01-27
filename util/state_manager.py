class StateManager:   
    def __init__(self):
        self.states = {}

    def add(self, name):
        self.states[name] = False

    def get_active(self):
        state_active = dict(filter(lambda w: w[1], self.states.items()))       
        return list(state_active.keys())[0] 

    def set_active(self, name):
        for key in self.states:           
            self.states[key] = key == name and True or False  