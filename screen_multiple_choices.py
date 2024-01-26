import tkinter as tk
import cv2
from util import utilities as utils
from util.scene_manager import SceneManager
from util.screen import Screen
from util.countdown import Countdown

from scenes.scene_master_page_multiple_choices import SceneMasterPageMultipleChoices
from scenes.scene_reading_multiple_choices import SceneReadingMultipleChoices

class ScreenMultipleChoices(Screen):    
    def __init__(self):        
        super().__init__("Quiz for Dummies!")       
               
         #scenes = SceneManager()

        #scenes.add("INIT")
        #scenes.add("READING")
        #scenes.add("COUNTDOWN")
        #scenes.add("RESPONDING")
        #scenes.add("TRANSITION")
        #scenes.add("END")
       
        self.scene_master_page = SceneMasterPageMultipleChoices(self)



        
        
        self.update_render()
        self.update_seconds()

        self.root.mainloop()
        

    def update_seconds(self):
        #self.countdown.update()

        if self.is_running:           
            self.root.after(1000, self.update_seconds) 


    def update_render(self):      
        self.scene_master_page.update_render()                       
        #self.root.after(30, self.update_render)  
        


   
  









   

if __name__ == "__main__":    
    player = ScreenMultipleChoices()
