#Ej13_carreras 
#ximena lizeeth sanchez arreola
#cbtis 89 

import tkinter as tk 
from tkinter import ttk

ventana=tk.Tk()
ventana.title("lista de desplegue conbobox")
ventana.geometry("300x400")

etiqueta=tk.Label (ventana, text="elegi una opcion")
etiqueta.pack(pady=10)

opciones={"ARH", "arquitectura", "comercio internacional y duanas"
"construccion", "contabilidad", "mecatronica", "programacion"}
combocolores=ttk.Button(ventana, values=opciones, state="readonly")
combocolores.pack(pady=10)

def mostrar_seleccion():
    seleccion=combocolores.get()
    etiqueta_res.config(text=f"seleccionaste: {seleccion:.2f}")

combocolores.bind("<<ComboboxSelected>>",mostrar_seleccion)

etiqueta_res=tk.Label(ventana, text="no has seleccionado nada mor")
etiqueta_res.pack(pady=10)

ventana.mainloop