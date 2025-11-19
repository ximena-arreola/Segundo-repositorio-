 # CBTIS 89
# ximena lizeeth sanchez arreola
# Programa  que on dos botones. Cada botón abrirá una ventana. 
# La primera ventana contendrá etiquetas con tu nombre y apellidos y
#  la segunda ventana tendrá el mensaje, «Programado con Python».# Crear la ventana principal
import tkinter as tk
from tkinter import Toplevel

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

# Función para abrir una ventana hija
def abrir_ventana_hija():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Ventana Hija")
    ventana_hija.geometry("250x150")
    
    etiqueta = tk.Label(ventana_hija, text="airam natalia", font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_hija, text="Cerrar", command=ventana_hija.destroy)
    boton_cerrar.pack(pady=10)
def abrir_ventana_hija2():
    ventana_hija2 = Toplevel(ventana_principal)
    ventana_hija2.title("Ventana Hija")
    ventana_hija2.geometry("250x150")
    
    etiqueta2= tk.Label(ventana_hija2, text="Programado con Python", font=("Arial", 12))
    etiqueta2.pack(pady=10)
    
    boton_cerrar2 = tk.Button(ventana_hija2, text="Cerrar", command=ventana_hija2.destroy)
    boton_cerrar2.pack(pady=10)


# Botón en la ventana principal para abrir la ventana hija
boton_abrir = tk.Button(ventana_principal, text="Tu nombre:", command=abrir_ventana_hija)
boton_abrir.pack(pady=20)

# Botón en la ventana principal para abrir la ventana hija
boton_abrir2 = tk.Button(ventana_principal, text="Programado", command=abrir_ventana_hija2)
boton_abrir2.pack(pady=20)

# Iniciar el loop principal
ventana_principal.mainloop()
