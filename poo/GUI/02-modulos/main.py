#import window
#from window import * #importar todo de el archivo
from window import Window,tk #modulo
#from functions import calculadora #package
from functions.calculadora import sumar #package

# Se puede importar paquetes de esta forma
# import functions.calculadora as calc
# calc.sumar()

# Importando modulos del paquete actual
# from .functions.calculadora import sumar 
# from .funciones import sumar as sumar2

# from .. import moduloPython #importando algo del paquete anterior 

root = Window()

frame1 = root.add_frame()
frame2 = root.add_frame()
label1 = tk.Label(frame1,text="Hola")
label1.pack()
label2 = tk.Label(frame2,text="Hola 2")
label2.pack()

root.window.mainloop()
