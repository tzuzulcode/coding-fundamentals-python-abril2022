import tkinter as tk

class Result:
    def __init__(self, frame):
        self.frame = frame

        self.frame.columnconfigure(0,weight=1)

    def add_label(self,bg,fg):
        output_label = tk.Label(
            self.frame,
            text="0",
            bg=bg,
            fg=fg,
            anchor='e',
            justify="right",
            font="Arial 50",
            padx=10
        )

        output_label.grid(row=0,column=0,sticky="NSEW")

    def write_number(self,number):
        pass