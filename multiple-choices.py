import tkinter as tk
import cv2
from PIL import Image, ImageTk

class Screen:
    def __init__(self, root, video_source=0, canvas_width=600, canvas_height=400):
        self.root = root
        self.counter = 0
        self.countdown = 5
        self.padding = 30
        self.max_width = canvas_width - self.padding
        self.root.geometry(f'{canvas_width}x{canvas_height}')
        self.root.title('Quiz for Dummies!')
        
        self.lines_quiz = self.break_text("Quiz".upper(), self.max_width)
        self.lines_for = self.break_text("for", self.max_width)
        self.lines_dummies = self.break_text("Dummies".upper(), self.max_width)

        self.lines_questions = self.break_text("O que é o que é, cai em pé e corre deitado?".upper(), self.max_width)

        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
        self.canvas.pack(anchor=tk.CENTER, expand=True)

        # Load the image
        self.question_mark_1 = self.load_image("./assets/images/question_mark_1.png", 0)
        self.question_mark_2 = self.load_image("./assets/images/question_mark_2.png", 0)
        self.question_mark_3 = self.load_image("./assets/images/question_mark_3.png", 0)
        self.question_mark_4 = self.load_image("./assets/images/question_mark_4.png", 0)
        self.question_mark_5 = self.load_image("./assets/images/question_mark_5.png", 0)
        self.question_mark_6 = self.load_image("./assets/images/question_mark_6.png", 0)

        self.video_source = video_source
        self.cap = cv2.VideoCapture(self.video_source)

        self.update_second_counter()
        self.update()

        self.root.mainloop()

    def update(self):
        ret, frame = self.cap.read()
        if ret:
             # Limpa o Canvas
            self.canvas.delete("all")
            # Redimensionar o frame para o tamanho do Canvas
            frame = cv2.resize(frame, (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()))

            self.photo = self.convert_to_tk_image(frame)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

            #self.image.rotate(12)
            # Render the image on the canvas
            self.canvas.create_image(340, 320, anchor=tk.CENTER, image=self.question_mark_1)
            self.canvas.create_image(20, 320, anchor=tk.CENTER, image=self.question_mark_2)
            self.canvas.create_image(350, 20, anchor=tk.CENTER, image=self.question_mark_4)
            self.canvas.create_image(350, 580, anchor=tk.CENTER, image=self.question_mark_2)
            self.canvas.create_image(30, 60, anchor=tk.CENTER, image=self.question_mark_6)
            self.canvas.create_image(30, 580, anchor=tk.CENTER, image=self.question_mark_5)

            self.render_text(self.lines_quiz, 0, 30, ("Jokerman", 16, "bold"), "black")
            self.render_text(self.lines_for, 0, 50, ("Jokerman", 8, "bold"), "black")
            self.render_text(self.lines_dummies, 0, 75, ("Jokerman", 20, "bold"), "black", (3, "white"), 12)
            self.render_text(self.lines_questions, 0, 150, ("Ink Free", 14, "bold"), "black")
            
            self.render_options(300, {'Chuva'.upper(): True, 'Mamão papaia'.upper(): False, 'Bicicleta'.upper(): True, })

            self.render_countdown()

            self.root.after(30, self.update)  # Atualiza a cada 30 milissegundos

          
           
        else:
            self.cap.release()

    def update_second_counter(self):
        # Atualiza o contador de 1 em 1 segundo
        self.counter += 1

        # Chama o método novamente após 1 segundo (1000 milissegundos)
        self.root.after(1000, self.update_second_counter)

    def render_countdown(self):
        text_width = self.canvas.winfo_reqwidth()
        text_x = text_width // 2
        text_y = 550
        r = 50

        #self.canvas.create_arc(text_x - r, text_y + r, text_x + r, text_y - r, start=0, extent=359, width=10, outline="red")
        #self.canvas.create_arc(text_x - r + 3, text_y + r - 3, text_x + r - 3, text_y - r + 3, start=0, extent=359, fill="#FFF1D5", outline="" )
        self.canvas.create_arc(text_x - r, text_y + r, text_x + r, text_y - r, start=0, extent=359, fill="#FFF1D5", outline="" )
        self.canvas.create_arc(text_x - r, text_y + r, text_x + r, text_y - r, start=0, extent=0, fill="#FFF100", outline="" )
        self.canvas.create_text(text_x, text_y, text=self.countdown, font=("Arial", 40, "bold"), fill="black", anchor=tk.CENTER)

        self.countdown = self.counter

    def load_image(self, image_path, rotation_angle=0):
        original_image = Image.open(image_path)        
        photo = ImageTk.PhotoImage(original_image)
        return photo  

    def render_options(self, y, responses):
        height = 50
        gap = height + 10
        for chave, valor in responses.items():
            self.round_rectangle(self.padding, y, self.max_width, y + height, radius=5, fill="#FFF1D5")
            self.render_text([chave], 0, y + (height / 2), ("Ink Free", 14, "bold"), "black")
            y += gap

    def convert_to_tk_image(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image=image)
        return photo

    def render_text(self, lines, x, y, font, fill, border=None, angle=0):
        text_width = self.canvas.winfo_reqwidth()
        text_height = self.canvas.winfo_reqheight()

        if x == 0: 
            text_x = text_width // 2
        else:
            text_x = x

        text_y = y #text_height // 2 - (len(lines) - 1) * 8  # Ajuste para centralizar a quebra de linha

        for line in lines:
            
            if(border != None):
                self.canvas.create_text(text_x + border[0], text_y, text=line, font=font, fill=border[1], anchor=tk.CENTER, angle=angle)
                self.canvas.create_text(text_x - border[0], text_y, text=line, font=font, fill=border[1], anchor=tk.CENTER, angle=angle)
                self.canvas.create_text(text_x , text_y + border[0], text=line, font=font, fill=border[1], anchor=tk.CENTER, angle=angle)
                self.canvas.create_text(text_x , text_y - border[0], text=line, font=font, fill=border[1], anchor=tk.CENTER, angle=angle)

            self.canvas.create_text(text_x, text_y, text=line, font=font, fill=fill, anchor=tk.CENTER, angle=angle)

            text_y += font[1] * 1.5  # Ajuste para espaçamento entre as linhas

    def break_text(self, text, max_width):
        words = text.split()
        lines = []
        current_line = words[0]

        for word in words[1:]:
            test_line = current_line + " " + word
            test_width = self.text_width(test_line, font=("Ink Free", 16, "bold"))
            if test_width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)
        return lines

    def text_width(self, text, **kwargs):
        # Função para calcular a largura do texto com uma determinada fonte
        temp_label = tk.Label(self.root, text=text, **kwargs)
        temp_label.update_idletasks()
        width = temp_label.winfo_reqwidth()
        temp_label.destroy()
        return width

    def round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
            
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        return self.canvas.create_polygon(points, **kwargs, smooth=True)

if __name__ == "__main__":
    root = tk.Tk()    
    player = Screen(root, './assets/videos/bg-green-animated-solar.mp4', canvas_width=370, canvas_height=650)
