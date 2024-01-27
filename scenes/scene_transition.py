from scenes.scene import Scene

class SceneTransition(Scene):

    def __init__(self, screen_instance):
        super().__init__(screen_instance, "TRANSITION")

        #self.questions = utils.break_text(self.screen_instance.root, "O que é o que é, cai em pé e corre deitado?".upper(), self.screen_instance.MAX_WIDTH)        
        #self.responses = {'Chuva'.upper(): True, 'Mamão papaia'.upper(): False, 'Bicicleta'.upper(): False }
       
    
    def update_seconds(self):
        pass    
    
    def update_render(self):
        pass        
        #self.render_question(self.questions)
        #self.render_options(self.responses)