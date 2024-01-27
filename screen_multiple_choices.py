import tkinter as tk
import cv2
from util import utilities as utils
from util.scene_manager import SceneManager
from util.screen import Screen
from util.countdown import Countdown

from scenes.scene_game_multiple_choices import SceneGameMultipleChoices
from scenes.scene_transition import SceneTransition

class ScreenMultipleChoices(Screen):    
    def __init__(self):        
        super().__init__("Quiz for Dummies!")       
               
        self.scene_manager = SceneManager()

        self.scene_manager.add("game", SceneGameMultipleChoices(self))
        self.scene_manager.add("transition", SceneTransition(self))

        self.scene_manager.set_active("game")

        self.update_render()
        self.update_seconds()

        self.root.mainloop()
        

    def update_seconds(self):
        #self.countdown.update()

        if self.is_running:           
            self.root.after(1000, self.update_seconds) 


    def update_render(self):
        scene = self.scene_manager.get_active()
        scene.update_render()
                              
        #self.root.after(30, self.update_render)     

if __name__ == "__main__":    
    player = ScreenMultipleChoices()
