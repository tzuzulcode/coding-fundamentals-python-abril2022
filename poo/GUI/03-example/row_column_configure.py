from curses import window
import tkinter as tk

window = tk.Tk()
window.title("Example")
window.geometry("640x480+500+500")
window.resizable(True,True)

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)
window.rowconfigure(1,weight=1)

label = tk.Label(window,text="Python",bg="#F2F4F3",fg="#49111C",font="Arial 50")
label2 = tk.Label(window,text="Tkinter",bg="#49111C",fg="#0A0908",font="Arial 50")
label3 = tk.Label(window,text="Tkinter",bg="#49111C",fg="#0A0908",font="Arial 50")

label.grid(row=0,column=0,sticky="NSEW")
label2.grid(row=1,column=0,sticky="NSEW")
label3.grid(row=0,column=1,sticky="NSEW")

window.mainloop()