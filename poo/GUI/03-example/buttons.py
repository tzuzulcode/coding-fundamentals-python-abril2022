from re import S
import tkinter as tk

class Buttons:
    def __init__(self,frame):
        self.frame = frame
        self.frame.rowconfigure(0,weight=1)
        self.frame.rowconfigure(1,weight=1)
        self.frame.rowconfigure(2,weight=1)
        self.frame.rowconfigure(3,weight=1)
        self.frame.rowconfigure(4,weight=1)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=1)
        self.frame.columnconfigure(2,weight=1)
        self.frame.columnconfigure(3,weight=1)

    def add_button(self,text,color,text_color,row,column,command,span=1):
        button = tk.Button(self.frame,text=text,bg=color,fg=text_color,borderwidth=0,relief="flat",highlightthickness=0,bd=0)
        button.configure(command=command)

        button.grid(row=row,column=column,sticky="NSEW",padx=0,pady=0,columnspan=span)
