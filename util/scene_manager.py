class SceneManager:   
    def __init__(self):
        self.scenes = {}

    def add(self, name):
        self.scenes[name] = False
    
    def set_active(self, name):
        for key in self.scenes:
            self.scenes[key] = key == name and True or False