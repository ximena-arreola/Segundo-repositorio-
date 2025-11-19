#Ej11_ventas
#ximena lizeeth sanchez arreola 
#cbtis 89

import tkinter as tk 
from  tkinter import messagebox

def articulos():
    try:
        can=float(entrada_cantidad.get())
        pre=float(entrada_precio.get())
        res=can*pre 
        resultado.config(text=f"resultado: {res:.2f}")
    except ValueError :
        messagebox.showwarning("error", "algo valido plis")

def iva():
    try:
        can=float(entrada_cantidad.get())
        pre=float(entrada_precio.get())
        res=can*pre 
        iva=res*0.16 
        resultado.config(text=f"resultado: {res:.2f}")
    except ValueError :
        messagebox.showwarning("error", "mor algo valido")

def total():
    try:
        can=float(entrada_cantidad.get())
        pre=float(entrada_precio.get())
        res=can*pre 
        iva=res*0.16
        total=res-iva 
        resultado.config(text=f"resultado: {res:.2f}")
    except ValueError :
        messagebox.showwarning("error", "ash ya bay")

ventana=tk. Tk ()
ventana.title 
ventana.geometry("400x500")

etiqueta=tk.Label(ventana, text="cantidad de articulos", font=("Arial", 14))
etiqueta.pack(pady=10)

entrada_cantidad=tk.Entry ()
entrada_cantidad.pack(pady=10)

etiqueta1=tk.Label(ventana, text="precio del articulo", font=("Arial", 14))
etiqueta1.pack(pady=10)

entrada_precio=tk.Entry()
entrada_precio.pack(pady=10)

boton_sub=tk.Button(ventana, text="subtotal", font=("Arial", 14))
boton_sub.pack(pady=5)

boton_iva=tk.Button(ventana, text="iva", font=("Arial", 14))
boton_iva.pack(pady=5)

boton_total=tk.Button(ventana, text="el total por fin", font=("Arial", 14))
boton_total.pack(pady=5)

etiqueta_resultado=tk.Label (
    ventana, 
    text="",
    font=("Arial", 14)
)

ventana.mainloop()