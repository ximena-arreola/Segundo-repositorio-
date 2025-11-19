# eJ14_RADIOBOTONES.PY
#ximena lizeeth sanchez arreola 
#cbtis 89

import tkinter as tk 
from tkinter import ttk

ventana=tk.Tk ()
ventana.title ("calcular descuentos")
ventana.geometry("300x400")
ventana.resizable(False, False)

etiqueta_cantidad=tk.Label(ventana, text="ingresa la cantidad:")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad=tk.Entry(ventana, justify="center")
entrada_cantidad.pack(pady=10)

def este_radio():
    opcion=seleccion.get()

    if opcion==1:
       can=float(entrada_cantidad.get()) 
       des=can*0.05
       etiqueta_res.config(text=f"hola mor obtuviste un descuento del 5%")

    elif opcion==2:
        can=float(entrada_cantidad.get())
        des=can*0.10
        etiqueta_res.config(text=f"hola mor obtuviste un descuento del 10%")

    elif opcion==3:
        can=float(entrada_cantidad.get())
        des=can*0.15
        etiqueta_res.config(tex=f"hola mor obtuviste un descuento del 15%")

seleccion=tk.IntVar()

radioB1=tk.Button(ventana, tex="descuento del 5%", variable=seleccion, value=1, command=ejecutar_radio)
radioB2=tk.Button(ventana, text="descuento del 10%",variable=seleccion, value=2, command=ejecutar_radio)
radioB3=tk.Button(ventana, text="descuento del 15%", variable=seleccion, value=3, command=ejecutar_radio)

radioB1.pack(pady=10)
radioB2.pack(pady=10)
radioB3.pack(pady=10)

etiqueta_res=tk.Label(ventana, text="", wraplength=350, justify="left")
etiqueta_res.pack(pady=10)

ventana.mainloop 