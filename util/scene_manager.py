class SceneManager:   
    def __init__(self):
        self.scenes = {}

    def add(self, name, scene):
        self.scenes[name] = scene

    def get_active(self):
        scene_active = dict(filter(lambda w: w[1].is_active, self.scenes.items()))       
        return list(scene_active.values())[0] 

    def set_active(self, name):
        for key in self.scenes:            
            self.scenes[key].is_active = key == name and True or False  