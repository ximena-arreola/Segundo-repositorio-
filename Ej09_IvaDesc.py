#Ej09_IvaDesc
#cbtis 89
#ximena lizeeth sanchez arreola

import tkinter as tk 
from tkinter import messagebox 
  
def calcular_iva ():
    try:
        cantidad=float (entrada_cantidad.get())
        iva=cantidad*0.16
        etiqueta_resultado.config(text=f"iva (16%): {iva:.2f}")
    except ValueError:
        messagebox.showerror("error", "por favor ingrese una cantidad valida.")

def calcular_descuento ():
    try:
        cantidad=float (entrada_cantidad.get())
        decs=cantidad *0.10
        etiqueta_resultado.config(text=f"desuento(10&): ${decs:.2f}")
    except ValueError:
        messagebox.showerror("error", "por favor ingrese una cantidad valida")

def calcular_total():
    try:
        cantidad=float(entrada_cantidad.get())
        iva=cantidad*0.16
        desc=cantidad *0.10
        total=cantidad+iva-desc
        etiqueta_resultado.config(text=f"total a pagar: ${total:.2f}")
    except ValueError:
        messagebox.showerror("error", "por favor ingrese una cantidad valida")
       

ventana =tk. Tk ()
ventana.title ("cxalcular iva y descuento")
ventana.geometry("300x200")
ventana.resizable(False,False)

etiqueta_cantidad= tk.Label(ventana, text="ingresa la cantidad:")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad= tk.Entry(ventana, justify="center")
entrada_cantidad.pack()

btn_iva=tk.Button(
    ventana,
    text="calcular iva",
    command=calcular_iva,
)
btn_iva.pack(pady=5)

btn_desc=tk.Button(
    ventana,
    text="calcular el descuento",
    command=calcular_descuento,
)
btn_desc.pack(pady=5)

btn_total =tk.Button (
    ventana,
    text="calcular total a apagar",
    command=calcular_total ,
)
btn_total.pack(pady=5)

etiqueta_resultado =tk.Label (
    ventana,
    text="",
    font=("Arial", 12, "bold")
)
etiqueta_resultado.pack(pady=15)

ventana.mainloop()