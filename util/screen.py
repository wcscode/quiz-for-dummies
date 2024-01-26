from abc import ABC, abstractmethod
import tkinter as tk

class Screen(ABC):
    def __init__(self, title):
        self.is_running = True
        self.CANVAS_WIDTH=370
        self.CANVAS_HEIGHT=650 
        self.root = tk.Tk()   
        self.root.title(title)

        self.background_video_image = {}

        self.background_video_image["photo"] = None
        self.PADDING = 30
        self.MAX_WIDTH = self.CANVAS_WIDTH - self.PADDING
        self.root.geometry(f'{self.CANVAS_WIDTH}x{self.CANVAS_HEIGHT}')        

        self.canvas = tk.Canvas(self.root, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg='white')
        self.canvas.pack(anchor=tk.CENTER, expand=True)

    @abstractmethod
    def update_seconds(self):
        pass
    
    @abstractmethod
    def update_render(self):
        pass