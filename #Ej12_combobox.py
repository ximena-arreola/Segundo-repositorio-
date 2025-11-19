#Ej12_combobox
#ximena lizeeth sanchez arreola 
#cbtis89

import tkinter as tk 
from tkinter import ttk

ventana= tk.Tk ()
ventana.title 
ventana.geometry

etiqueta=tk.Label(ventana, text="elige una opcion")
etiqueta.pack(pady=10)

opciones=("rojo", "verde", "rosita", "moradito", "lila")
comboColores=tk.Button(ventana, values=opciones, state="readnoly")
comboColores.pack(pady=5)

def mostrar_seleccion():
    seleccion=comboColores.get()
    etiqueta_resultado.config(text=f"seleccionaste: {seleccion:.2f}")

comboColores.bind("<<comboseleccion>>",mostrar_seleccion)

etiqueta_resultado=tk.Label(ventana, text="aun no has seleccionado nada mor")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()