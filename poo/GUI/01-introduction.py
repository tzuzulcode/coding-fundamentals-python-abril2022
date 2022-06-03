import tkinter as tk
#from tkinter import *

# master widget
window = tk.Tk() # widget que referencía a la ventana raiz
window.title("Primer programa")
window.geometry("500x300+300+300") # WIDTHxHEIGHT+POSITIONX+POSITIONY
window.resizable(True,False) # WIDTH,HEIGHT

# label -> etiqueta
# Label -> widget que muestra texto
label = tk.Label(
    window, 
    text="Hola mundo",
    font=('Arial 23 bold'),# font(Estilo de letra)
    bg='#C1D7AE', # Background (Color de fondo)
    fg='#8CC084' # Foreground(Color del texto)
)

name_label = tk.Label(window,text="Ingresa tu nombre:")
name_input = tk.Entry(window) # input
cats_input = tk.Checkbutton(window,text="Click si tienes gatos!!") # checkbox

number_label = tk.Label(window,text="Cuantos gatos tienes?")
number_of_cats = tk.Spinbox(window,from_=0,to=100,increment=1)

# pady=(top,bottom), padx=(left,right)
# pady=(arriba,abajo), padx=(izquierda,derecha)
label.grid(columnspan=2, pady=(0,10), ipady=20, ipadx=20,sticky=(tk.W+tk.E)) # Colocamos el elemento en la interfaz
name_label.grid(row=1,column=0, padx=50,pady=20)
name_input.grid(row=1,column=1)
cats_input.grid(row=2,column=1)
number_label.grid(row=3,column=0)
number_of_cats.grid(row=3,column=1, padx=50, pady=20)


window.mainloop() # Inicia el ciclo de eventos de la app.