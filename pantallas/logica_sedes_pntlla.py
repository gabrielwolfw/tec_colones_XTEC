from tkinter import messagebox
import tkinter as tk

from administacion_sedes import Sedes

sedes = Sedes()

def crear_sede(nombre_entry, ubicacion_entry, numero_contacto_entry, estado_var):          
    nombre = nombre_entry.get()
    ubicacion = ubicacion_entry.get()
    numero_contacto = numero_contacto_entry.get()
    estado = estado_var.get()

    if sedes.validar_input_sede(nombre, ubicacion, numero_contacto):
        sedes.crear_sede(nombre, ubicacion, numero_contacto, estado)
        messagebox.showinfo("Éxito", "Sede creada exitosamente")

        limpiar_campos(nombre_entry, ubicacion_entry, numero_contacto_entry, estado_var)
    else:
        messagebox.showerror("Error", "No se pudo crear la sede")

def limpiar_campos(nombre_entry, ubicacion_entry, numero_contacto_entry, estado_var):
    nombre_entry.delete(0, tk.END)
    ubicacion_entry.set('')  # Limpiar el cuadro combinado (Combobox)
    numero_contacto_entry.delete(0, tk.END)
    estado_var.set("activo")  # Restablecer el valor predeterminado del OptionMenu

