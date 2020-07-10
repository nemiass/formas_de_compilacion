from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

#LABEL NOS SIRVE PARA MOSTRAR TEXTO O INTERFAZ GRAFICA 

label = Label(ventana)
label.pack()


#CONFIGS, resordar que estos configs son parametros de Label()
# contenido de texto, color de fondo del label, color de fuente
label.config(text="Hola Mundo") #Contenido del label
label.config(bg="skyblue")
label.config(fg="yellow")

#Tipo de fuente y tamaño
label.config(font=("Arial",30))


"""
	Metodos del label Cget() -> nos devuelve el dato  de cualquier parametro del label que le pasemos
	Configure() -> nos devuelve el dato  de cualquier parametro del label que le pasemos en forma de tupla
"""

#VARIABLE, METODOS SET Y GET, establecemos valor y recuperamos contenido de una label
texto = StringVar()
texto.set("Hola mundo")

texto2 = StringVar()
texto2.set(texto.get()) #recuperamos el contenido de nuestra label2 y la pasamos al label3

label2 = Label(ventana, text="Hey")
label2.pack(side="right")
label2.config(textvariable=texto)

label3 = Label(ventana, text="ga")
label3.pack(side="left")
label3.config(textvariable=texto2)

#Funcion que devuelve rutas, metodo 1
import os, sys
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

#Funcion que devuelve rutas, metodo 2, el que funciona mejor
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

imgg = resource_path("morty.gif")

#COLOCANDO IMAGEN EN LABEL
# Creamos nuestra variable imagen pra guardar nuestra imagen
imagen = PhotoImage(file=imgg)

# pasamos la imagen label por uno de sus parametros llamado image
Label(ventana, image=imagen).pack()

"""
	OTRO METODO ESTILO PACK() Y PLACE() ES "GRID()"

	Parametros de grid():
	-row -> indicamos fila en que se posicionara
	-column -< indicamos columna en que se posicionara
	-padx -> padding en el eje x
	-pady -< padding en el eje y
	-sticky = (e,w)-> posicionamos nuestro contenido del label, este u oeste

"""


ventana.mainloop()