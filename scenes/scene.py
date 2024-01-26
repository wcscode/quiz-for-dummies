from abc import ABC, abstractmethod

class Scene(ABC):
    def __init__(self, screen_instance, name):
        self.root = screen_instance.root
        self.canvas = screen_instance.canvas
        self.name = name        
        

    @abstractmethod
    def update_seconds(self):
        pass
    
    @abstractmethod
    def update_render(self):
        pass