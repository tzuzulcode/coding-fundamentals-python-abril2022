import tkinter as tk

class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Modulos")
        self.window.geometry("500x300+300+300") # WIDTHxHEIGHT+POSITIONX+POSITIONY
        self.window.resizable(True,False)

    def add_frame(self):
        frame = tk.Frame(self.window)
        frame.pack()

        return frame

        