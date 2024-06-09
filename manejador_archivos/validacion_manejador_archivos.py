import os
from tkinter import messagebox

def validar_existencia_archivo_transacciones():
    if not os.path.exists("./base_datos/transacciones.txt"):
        messagebox.showerror("Error", "El archivo transacciones.txt no existe. Por favor, comuníquese con el administrador del sistema.")
        return

def validar_existencia_archivo_centros_acopio():
    if not os.path.exists("./base_datos/centrosacopio.txt"):
        messagebox.showerror("Error", "El archivo centrosacopio.txt no existe. Por favor, comuníquese con el administrador del sistema.")
        return

def validar_existencia_archivo_materiales():
    if not os.path.exists("./base_datos/materiales.txt"):
        messagebox.showerror("Error", "El archivo materiales.txt no existe. Por favor, comuníquese con el administrador del sistema.")
        return
    
def validar_existneia_archivo_sedes():
    if not os.path.exists("./base_datos/sedes.txt"):
        messagebox.showerror("Error", "El archivo sedes.txt no existe. Por favor, comuníquese con el administrador del sistema.")
        return False
    return True