from tkinter import messagebox
import tkinter as tk

from administacion_sedes import Sedes

sedes = Sedes()

def crear_sede(nombre_entry, ubicacion_entry, numero_contacto_entry, estado_var):          
    nombre = nombre_entry.get()
    ubicacion = ubicacion_entry.get()
    numero_contacto = numero_contacto_entry.get()
    estado = estado_var.get()

    if validar_input_sede(nombre, ubicacion, numero_contacto):
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


def validar_input_sede(nombre, ubicacion, numero_contacto):
    try:
        if not 1 <= len(nombre) <= 50:
            messagebox.showerror("Error", "El nombre de la sede debe tener entre 5 y 50 caracteres")
            return False

        if not 5 <= len(ubicacion) <= 50:
            messagebox.showerror("Error", "La ubicación debe tener entre 5 y 50 caracteres")
            return False

        if not numero_contacto.isdigit() or not 1000000 < int(numero_contacto) < 100000000:
            messagebox.showerror("Error", "El número de contacto debe tener 8 dígitos")
            return False
        return True
    except ValueError:
        messagebox.showerror("Error", "El número de contacto debe ser un valor numérico válido.")
        return False
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {str(e)}")
        return False
