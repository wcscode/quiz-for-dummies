import tkinter as tk
import cv2
from PIL import Image, ImageTk

def load_image(image_path):
    original_image = Image.open(image_path)        
    photo = ImageTk.PhotoImage(original_image)
    return photo

def convert_to_tk_image(frame):   
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   
    image = Image.fromarray(image)    
    return ImageTk.PhotoImage(image=image)

def video_capture(path):
    return cv2.VideoCapture(path)

def render_background_video(canvas, frame, background_video_image):
    frame = cv2.resize(frame, (canvas.winfo_reqwidth(), canvas.winfo_reqheight()))    
    background_video_image["photo"] = convert_to_tk_image(frame)
    return canvas.create_image(0, 0, anchor=tk.NW, image=background_video_image["photo"])

def render_text(canvas, lines, x, y, font, fill, border=None, angle=0):
    text_width = canvas.winfo_reqwidth()
    text_height = canvas.winfo_reqheight()

    if x == 0: 
        text_x = text_width // 2
    else:
        text_x = x

    text_y = y #text_height // 2 - (len(lines) - 1) * 8  # Ajuste para centralizar a quebra de linha

    for line in lines:
        
        if(border != None):
            canvas.create_text(text_x + border[0], text_y, text=line, font=font, fill=border[1], anchor=tk.CENTER, angle=angle)
            canvas.create_text(text_x - border[0], text_y, text=line, font=font, fill=border[1], anchor=tk.CENTER, angle=angle)
            canvas.create_text(text_x , text_y + border[0], text=line, font=font, fill=border[1], anchor=tk.CENTER, angle=angle)
            canvas.create_text(text_x , text_y - border[0], text=line, font=font, fill=border[1], anchor=tk.CENTER, angle=angle)

        canvas.create_text(text_x, text_y, text=line, font=font, fill=fill, anchor=tk.CENTER, angle=angle)

        text_y += font[1] * 1.5  # Ajuste para espaçamento entre as linhas

def break_text(root, text, max_width):
    words = text.split()
    lines = []
    current_line = words[0]

    for word in words[1:]:
        test_line = current_line + " " + word
        test_width = text_width(root, test_line, font=("Ink Free", 16, "bold"))
        if test_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines

def text_width(root, text, **kwargs):
    # Função para calcular a largura do texto com uma determinada fonte
    temp_label = tk.Label(root, text=text, **kwargs)
    temp_label.update_idletasks()
    width = temp_label.winfo_reqwidth()
    temp_label.destroy()

    return width

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
        
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

    return canvas.create_polygon(points, **kwargs, smooth=True)
