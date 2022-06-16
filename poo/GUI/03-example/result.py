from cgitb import text
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

        self.output_label = output_label

    def write_number(self,number,calculator):
        if(calculator.active_number==1):
            if(calculator.number1=="0"):
                calculator.number1 = str(number)
            else:
                calculator.number1 = calculator.number1 + str(number)
            self.output_label.configure(text=calculator.number1)
        else:
            if(calculator.number2=="0"):
                calculator.number2 = str(number)
            else:
                calculator.number2 += str(number)
            self.output_label.configure(text=calculator.number2)

    def update_result(self,calculator):
        print(calculator.number1)
        self.output_label.configure(text=calculator.number1)