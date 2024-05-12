from tkinter import messagebox

from administacion_sedes import Sedes

sedes = Sedes()

def crear_sede(nombre, ubicacion, numero_contacto, estado):
    if sedes.validar_input_sede(nombre, ubicacion, numero_contacto):
        sedes.crear_sede(nombre, ubicacion, numero_contacto, estado)
        messagebox.showinfo("Éxito", "Sede creada exitosamente")
    else:
        messagebox.showerror("Error", "No se pudo crear la sede")



