import tkinter as tk
#from tkinter import *


# master widget
window = tk.Tk() # widget que referencía a la ventana raiz
window.title("Primer programa")
window.geometry("500x300+300+300") # WIDTHxHEIGHT+POSITIONX+POSITIONY
window.resizable(True,False) # WIDTH,HEIGHT
checked = tk.BooleanVar()

# Frames
title_frame = tk.Frame(window) # pack
form_frame = tk.Frame(window) # grid

# label -> etiqueta
# Label -> widget que muestra texto
title = tk.Label(
    title_frame, 
    text="Hola mundo",
    font=('Arial 50 bold'),# font(Estilo de letra)
    bg='#C1D7AE', # Background (Color de fondo)
    fg='#8CC084', # Foreground(Color del texto)
    anchor='w', # De que lado del widget se colocara el texto
    justify='left', # Justificación del texto: center, left o right
)

name_label = tk.Label(form_frame,text="Ingresa tu nombre:")
name_input = tk.Entry(form_frame) # input
cats_input = tk.Checkbutton(form_frame,text="Click si tienes gatos!!", variable=checked) # checkbox

number_label = tk.Label(form_frame,text="Cuantos gatos tienes?")
number_of_cats = tk.Spinbox(form_frame,from_=0,to=100,increment=1)

submit_button = tk.Button(form_frame, text="Enviar datos")

output_line = tk.Label(window,text='')

# pady=(top,bottom), padx=(left,right)
# pady=(arriba,abajo), padx=(izquierda,derecha)
# title.grid(columnspan=2, pady=(0,10), ipady=20, ipadx=20,sticky=(tk.W+tk.E)) # Colocamos el elemento en la interfaz
title.pack(fill="x") # Colocamos el elemento en la interfaz
name_label.grid(row=1,column=0, padx=50,pady=20)
name_input.grid(row=1,column=1)
cats_input.grid(row=2,column=1)
number_label.grid(row=3,column=0)
number_of_cats.grid(row=3,column=1, padx=50, pady=20)
submit_button.grid(row=4,column=0, columnspan=2, sticky=(tk.W+tk.E), ipady=10)


title_frame.pack(fill="x")
form_frame.pack(fill="x")
output_line.pack()


def on_submit():
    name = name_input.get()
    has_cats = cats_input.getboolean(checked.get())
    number_cats = int(number_of_cats.get())

    if has_cats:
        message = f"Hola, bienvenido {name}. Tienes {number_cats} gatos."
        output_line.configure(text=message)
    else:
        message = "Hola, bienvenido "+name
        output_line.configure(text=message)
        
submit_button.configure(command=on_submit)

window.mainloop() # Inicia el ciclo de eventos de la app.