from tkinter import messagebox
import tkinter as tk
from administacion_sedes import CentrosAcopio

centro_acopio = CentrosAcopio()

def crear_centro_acopio(sede_entry, numero_contacto_entry, identificador_entry):
    sede = sede_entry.get()
    numero_contacto = numero_contacto_entry.get()
    identificador = identificador_entry.get()

    if validar_input_centro_acopio(sede, numero_contacto, identificador):
        centro_acopio.crear_centro_acopio(sede, numero_contacto, identificador)
        messagebox.showinfo("Éxito", "Centro de acopio creado exitosamente")

        limpiar_campos(sede_entry, numero_contacto_entry, identificador_entry)

    else:
        messagebox.showerror("Error", "No se pudo crear el centro de acopio")

def limpiar_campos(sede_entry, numero_contacto_entry, identificador_entry):
    sede_entry.delete(0, tk.END)
    numero_contacto_entry.delete(0, tk.END)
    identificador_entry.delete(0, tk.END)


def validar_input_centro_acopio(sede, numero_contacto, identificador):
    try:
        if sede not in centro_acopio.sedes_existentes:
            messagebox.showerror("Error", "La sede no existe")
            return False
        if not numero_contacto.isdigit() or not 10000000 <= int(numero_contacto) <= 99999999:
            messagebox.showerror("Error", "El número de contacto debe ser un número de 8 dígitos")
            return False
        if identificador in centro_acopio.identificadores_existentes:
            messagebox.showerror("Error", "El identificador ya existe")
            return False
        # Verificar si el identificador ya existe en la lista de centros de acopio
        for centro_acopio_ in centro_acopio.centros_acopio:
            if centro_acopio_["Identificador"] == identificador:
                messagebox.showerror("Error", "Ya existe un centro de acopio con ese identificador")
                return False
        return True
    except ValueError:
        messagebox.showerror("Error", "El número de contacto debe ser un valor numérico válido.")
        return False
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {str(e)}")
        return False