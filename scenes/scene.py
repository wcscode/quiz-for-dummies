from abc import ABC, abstractmethod

class Scene(ABC):
    def __init__(self, screen_instance, name): 
        self.is_active = False       
        self.screen_instance = screen_instance
        self.name = name        
        

    @abstractmethod
    def update_seconds(self):
        pass
    
    @abstractmethod
    def update_render(self):
        pass