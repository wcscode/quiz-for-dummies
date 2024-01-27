import tkinter as tk
from util import utilities as utils
from scenes.scene import Scene
from util.state_manager import StateManager

class SceneGameMultipleChoices(Scene):

    def __init__(self, screen_instance):
        super().__init__(screen_instance, "ALL")   

        self.video_capture = utils.video_capture('./assets/videos/bg-green-animated-solar.mp4')         

        self.backgrounds_questions = {}        

        for i in range(1, 7, 1):
            self.backgrounds_questions[f"question_mark_{i}"] = utils.load_image(f"./assets/images/question_mark_{i}.png")
   
        self.headers = {}

        self.headers["quiz"] = utils.break_text(self.screen_instance.root, "QUIZ", self.screen_instance.MAX_WIDTH)
        self.headers["for"] = utils.break_text(self.screen_instance.root, "for", self.screen_instance.MAX_WIDTH)
        self.headers["dummies"] = utils.break_text(self.screen_instance.root, "DUMMIES", self.screen_instance.MAX_WIDTH)       

        self.questions = utils.break_text(self.screen_instance.root, "O que é o que é, cai em pé e corre deitado?".upper(), self.screen_instance.MAX_WIDTH)        
        self.responses = {'Chuva'.upper(): True, 'Mamão papaia'.upper(): False, 'Bicicleta'.upper(): False }

        self.state_manager = StateManager()

        self.state_manager.add("load_questions")
        self.state_manager.add("reading")
        self.state_manager.add("countdown")
        self.state_manager.add("responding")

        
        #self.countdown = Countdown(self.canvas, 5)

    def update_seconds(self):
        pass    
    
    def update_render(self):

        #ret, frame = self.video_capture.read()
        #if ret:  
        #    utils.render_background_video(self.screen_instance.canvas, frame, self.background_video_image)                                

        ret, frame = self.video_capture.read()
        if ret:  
            self.screen_instance.canvas.delete("all")

            #self.scene_master_page.update_render()
            self.render_header_text(0, 30, "quiz", 16)
            self.render_header_text(0, 50, "for", 8)
            self.render_header_text(0, 75, "dummies", 20, True)    

            self.render_question_mark(340, 320, "question_mark_1")
            self.render_question_mark(20, 320, "question_mark_2")
            self.render_question_mark(350, 20, "question_mark_4")
            self.render_question_mark(350, 580, "question_mark_2")
            self.render_question_mark(30, 60, "question_mark_6")
            self.render_question_mark(30, 580, "question_mark_5")  

            self.render_question(self.questions)

            self.render_options(self.responses)

            #self.countdown.render()            
           
            self.screen_instance.root.after(30, self.update_render)  
        else:
            self.video_capture.release()
            self.is_running = False

   

    def render_header_text(self, x, y, name, font_size, border=False):
        if border:
            utils.render_text(self.screen_instance.canvas, self.headers[name], x, y, ("Jokerman", font_size, "bold"), "black", (3, "white"), 12)
        else:
            utils.render_text(self.screen_instance.canvas, self.headers[name], x, y, ("Jokerman", font_size, "bold"), "black")

    def render_question_mark(self, x, y, name):
        self.screen_instance.canvas.create_image(x, y, anchor=tk.CENTER, image=self.backgrounds_questions[name])            

    def render_question(self, questions):
        utils.render_text(self.screen_instance.canvas, questions, 0, 150, ("Ink Free", 14, "bold"), "black")

    def render_options(self, responses):
        y = 300
        height = 50
        gap = height + 10
        for chave, valor in responses.items():
            fill = valor == False and "#FFF1D5" or "#FFEB0F"
            utils.round_rectangle(self.screen_instance.canvas, self.screen_instance.PADDING, y, self.screen_instance.MAX_WIDTH, y + height, radius=5, fill=fill)
            utils.render_text(self.screen_instance.canvas, [chave], 0, y + (height / 2), ("Ink Free", 14, "bold"), "black")
            y += gap
