#ximena lizeeth sanchez arreola
#Programacion 3°B
#cbtis 89

import tkinter as tk
from tkinter import messagebox

def calcular_sueldoi():
    try:
        nombre = entrada_nom.get()
        sueldo = float(entrada_sueldo.get())
        meses = int(entrada_meses.get())

        if nombre == "" or sueldo <= 0 or meses < 0 or meses > 12:
            raise ValueError

        #sueldo por meses trabajados
        sueldo_por_meses = sueldo * meses

        #aguinaldo: solo si trabajó 3 meses o más
        if meses >= 3:
            aguinaldo = sueldo / 2
        else:
            aguinaldo = 0

        #subtotal
        subtotal = sueldo_por_meses + aguinaldo

        #bono anual según tipo
        if bono_varl.get() == 1:
            bono_anual = subtotal * 0.10
        elif bono_varl.get() == 2:
            bono_anual = subtotal * 0.05
        else:
            bono_anual = 0

        # Sueldo total anual
        total = subtotal + bono_anual

        # Mostrar resultado
        resultado.config(text=f"""
Nombre del trabajador: {nombre}
Sueldo por meses: ${sueldo_por_meses:,.2f}
Aguinaldo: ${aguinaldo:,.2f}
Subtotal: ${subtotal:,.2f}
Bono anual: ${bono_anual:,.2f}
---------------------------------
SUELDO TOTAL ANUAL: ${total:,.2f}
""")

    except ValueError:
        messagebox.showerror("Error", "Verifica que los datos ingresados sean validos mor, plis .")


# Ventana principal
ventana = tk.Tk()
ventana.title("cálculo del sueldo total anual")
ventana.geometry("420x450")

# Entradas
tk.Label(ventana, text="nombre del trabajador:").pack()
entrada_nom = tk.Entry(ventana)
entrada_nom.pack()

tk.Label(ventana, text="sueldo mensual:").pack()
entrada_sueldo = tk.Entry(ventana)
entrada_sueldo.pack()

tk.Label(ventana, text="meses trabajados (0-12):").pack()
entrada_meses = tk.Entry(ventana)
entrada_meses.pack()

# Radio buttons de bono
tk.Label(ventana, text="\ntipo de bono anual:").pack()
bono_varl = tk.IntVar()
tk.Radiobutton(ventana, text="completo (10%)", variable=bono_varl, value=1).pack()
tk.Radiobutton(ventana, text="parcial (5%)", variable=bono_varl, value=2).pack()
tk.Radiobutton(ventana, text="sin Bono (0%)", variable=bono_varl, value=3).pack()

# Botón
tk.Button(ventana, text="calcular sueldo total anual", command=calcular_sueldoi).pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="", justify="left", font=("Arial", 12))
resultado.pack()

ventana.mainloop()
