 # CBTIS 89
# ximena lizeeth sanchez arreola
# 3°B Programa T.M
# Programa  que cantidad es el dolares 
import tkinter as tk
from  tkinter import messagebox 
def calcular_dolares():
  try:
   cantidad=float(entrada_cantidad.get())
   dolares=cantidad*0.054
   etiqueta_resultado.config(text=f"El dolar equivale a 0.054 que son :${dolares:.2f}")

  except ValueError:
     messagebox.showerror("error","por favor ingresa una cantidad valida :")

def calcular_euros():
  try :
   cantidad=float(entrada_cantidad.get())
   euros=cantidad*0.47
   etiqueta_resultado.config(text=f"El euro equibale a  0.47 que son  :${euros:.2f}")
  except ValueError: 
       messagebox.showerror("error","por favor ingrese una cantidad valida:")
def calcular_libras():
  try:
    cantidad=float(entrada_cantidad.get())
    libras=cantidad*0.041
    etiqueta_resultado.config(text=f"La libras equivale a 0.041 que son :${libras:.2f}")
  except ValueError:
       messagebox.showerror("error","por favor ingrese una cantidad valida:")
def calcular_yenes():
  try:
    cantidad=float(entrada_cantidad.get())
    yenes=cantidad*8.21
    etiqueta_resultado.config(text=f"La libras equivale a 8.21 que son :${yenes:.2f}")
  except ValueError:
       messagebox.showerror("error","por favor ingrese una cantidad valida:")
ventana=tk.Tk()
ventana.title("DIVISAS ")
ventana.geometry("500x250")
ventana.resizable(False,False)

etiqueta_cantidad=tk.Label(ventana,text="ingresa la cantidad:")
etiqueta_cantidad.pack(pady=10)
entrada_cantidad=tk.Entry(ventana,text="Ingresa la cantidad:")
entrada_cantidad.pack()

btn_dolares=tk.Button(
  ventana,
  text="calcular dolares",
  command=calcular_dolares,
  )
      
btn_dolares.pack(pady=5)
     
btn_euros=tk.Button(
  ventana,
  text="calcular Euros",
  command=calcular_euros,
  
 )
btn_euros.pack(pady=5)

btn_libras=tk.Button(
  ventana,
  text="Calcular libras",
  command=calcular_libras,
 
)
btn_libras.pack(pady=5) 

btn_yenes=tk.Button(
  ventana,
  text="Calcular yenes",
  command=calcular_yenes,
 
)
btn_yenes.pack(pady=5)

etiqueta_resultado=tk.Label(
  ventana,
  text=" ",
  font=("Arial",12,"bold")                                                     
)
etiqueta_resultado.pack(pady=15)
ventana.mainloop()