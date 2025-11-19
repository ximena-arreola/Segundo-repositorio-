#Ej08_ventanaexplicacion
#ximena lizeeth sanchez arreola
#cbtis 89
#programacion 3b 
 
#importamos la libreria tkinter y le damos un alias "tk"
import tkinter as tk

#crear la ventana principal 
ventana =tk.Tk()

# configurar el titulo de la ventana
ventana.title("ventana de saludo")

#definir el tamaño de la ventana
ventana.geometry("400x300")

#agregar un texto (etiqueta)
etiqueta =tk.Label (ventana,text="holaaa menos dias ", font=("arial,16"))
etiqueta.pack(pady=20)

#agregar un boton 
def saludar ():
    etiqueta.config(text="como vash en tu dia?")
boton=tk.Button(ventana, text="saludar", command=saludar)
boton.pack(pady=10)

#ejecutar el bucle principaln de la aplicacion
ventana.mainloop()