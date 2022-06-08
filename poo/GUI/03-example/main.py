import tkinter as tk
from buttons import Buttons

window = tk.Tk()
window.title("Example")
window.geometry("220x300+500+500")
window.resizable(True,True)

window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=5)

input_frame = tk.Frame(window)
buttons_frame = tk.Frame(window)


input_frame.grid(row=0,column=0,sticky="NSEW")
buttons_frame.grid(row=1,column=0,sticky="NSEW")


buttons = Buttons(buttons_frame)
buttons.add_button("+","#55688F","white",0,0)
buttons.add_button("-","#55688F","white",0,1)
buttons.add_button("*","#55688F","white",1,0)
buttons.add_button("/","#55688F","white",1,1)

window.mainloop()