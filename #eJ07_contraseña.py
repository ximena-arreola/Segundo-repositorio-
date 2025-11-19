#eJ07_contraseña
#cbtis 89
#ximena lizeeth sanchez arreola 

import tkinter as tk 
from tkinter import messagebox
from tkinter import font 

def abrir_ventana_principal ():
    ventana_principal =tk.Toplevel()
    ventana_principal.title ("menu principal")
    ventana_principal.geometry("400x300")


    etiqueta_bienvenida=tk.Label (
        ventana_principal,
        text="bienvenido al sistema",
        font=("Arial", 14),
    ) 
    etiqueta_bienvenida.pack(pady=40)

    boton_salir=tk.Button(
        ventana_principal ,
        text="cerrar sesion",
        font=("Arial", 14),
        command=lambda:(
            ventana_principal.destroy(),
            ventana.deiconify()
        )

    )
    boton_salir.pack(pady=20)

#funcion para virificar la contraseña 
def verificar_contraseña ():
    contraseña= entrada_contraseña.get()
    if contraseña =="mena123":
        messagebox.showinfo("acceso","acceso correcto")

        #oculta la ventana de login 
        ventana.withdraw()
        
        #abre la ventana principal 
        abrir_ventana_principal()
    else:
        messagebox.showerror("acceso","acceso denegado")
#crear ventana login
ventana=tk.Tk()
ventana.title("sistema de acceso")
ventana.geometry("350x200")
 
fuente_titulo = font.Font(family="arial", size=14)
fuente_normal =font.Font(family="arial", size=14)

marco=tk.Frame(ventana,bd=2, relief="groove")
marco.place(relx=0.5, rely=0.5, anchor="center")

etiqueta=tk.Label(marco, text="ingrese su contraseña", font=fuente_titulo)
etiqueta.pack(padx=20, pady=(15,5))

entrada_contraseña = tk.Entry(marco, show="*", font=fuente_normal, width=25, bd=2, relief="solid")
entrada_contraseña.pack(pady=5,padx=20)

boton_verificar = tk.Button(
   marco,
   text="verificar acceso",
   command=verificar_contraseña,
   padx=10,
   pady=5,
   relief="flat"
)
boton_verificar.pack(pady=(10,15))

ventana.mainloop()