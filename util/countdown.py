import tkinter as tk

class Countdown:
    def __init__(self, canvas, start_number): 
        self.canvas = canvas       
        self.start_number = start_number
        self.current_number = start_number
        self.counter = 0
    
    def get_current_number(self):
        return self.current_number
       
    def update(self):
        if self.current_number > 0:
            self.current_number += -1
            self.counter += 1

    def reset(self):
        self.current_number = self.start_number
        self.counter = 0

    def render(self, x = 0, y = 550):
        text_width = self.canvas.winfo_reqwidth()
        x = x == 0 and text_width // 2 or x        
        r = 50
        
        self.canvas.create_arc(x - r, y + r, x + r, y - r, start=0, extent=359, fill="#FFF1D5", outline="" )
        self.canvas.create_arc(x - r, y + r, x + r, y - r, start=0, extent=((360/self.start_number) * self.counter) -1, fill="#FFF100", outline="" )
        self.canvas.create_text(x, y, text=self.current_number, font=("Arial", 40, "bold"), fill="black", anchor=tk.CENTER)
