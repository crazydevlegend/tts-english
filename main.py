import pyttsx3
import threading
from tkinter import *
from tkinter import ttk, filedialog


def open_file():
    global text

    file = filedialog.askopenfile(
        mode='r', filetypes=[('Text Files', '*.txt')])
    if file:
        text = file.read()
        label.config(text=text)
        file.close()


def play_audio():
    play_button['text'] = "Playing..."
    thread = tts_speaker(text)
    thread.start()
    play_button['text'] = "Play"


class tts_speaker(threading.Thread):
    def __init__(self, text):
        threading.Thread.__init__(self)
        self.engine = pyttsx3.init()
        self.text = text

        # helper function to execute the threads
    def run(self):
        self.engine.say(text)
        self.engine.runAndWait()


text = "Here we go!!!\nPlease browse a text file you want to read"
win = Tk()
win.geometry("700x350")
win.title("TTS app by @crazydevlegend")

# Create <Browse> Button
browse_button = ttk.Button(win, text="Browse", command=open_file)
browse_button.pack()
# Create <Play> Button
play_button = ttk.Button(win, text="Play", command=play_audio)
play_button.pack()

# Add a Label widget
label = Label(win, text=text,
              font=('Georgia 13'))
label.bind('<Configure>', lambda e: label.config(
    wraplength=win.winfo_width()))
label.pack(pady=10)


win.mainloop()
