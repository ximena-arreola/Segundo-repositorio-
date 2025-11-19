#Ej03_NomAp
#programacion 3b
#ximena lizeeth sanchez arreola
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Widgets en Tkinter")
ventana.geometry("300x200")

# Etiqueta de texto
etiqueta = tk.Label(ventana, text="Nombre y apellido", font=("Arial", 12))
etiqueta.pack(pady=10)

# Cuadro de texto
entrada1 = tk.Entry(ventana, font=("Arial", 12))
entrada1.pack(pady=5)
entrada2=tk.entry (ventana,font=("arial",12))
entrada2.pack(pady=5)

# Botón que responde a un evento
def mostrar_nombre ():
    texto1 = entrada1.get()
    texto2 = entrada2.get()
    etiqueta_resultado.config (text=f"{texto1}{texto2}")

boton = tk.Button(ventana, text="Mostrar nombre", command=mostrar_nombre)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=5)

# Iniciar el loop principal
ventana.mainloop()
