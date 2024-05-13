from tkinter import messagebox
import tkinter as tk
from administacion_sedes import CentrosAcopio

centro_acopio = CentrosAcopio()

def crear_centro_acopio(sede_entry, numero_contacto_entry, identificador_entry):
    sede = sede_entry.get()
    numero_contacto = numero_contacto_entry.get()
    identificador = identificador_entry.get()

    if centro_acopio.validar_input_centro_acopio(sede, numero_contacto, identificador):
        centro_acopio.crear_centro_acopio(sede, numero_contacto, identificador)
        messagebox.showinfo("Éxito", "Centro de acopio creado exitosamente")

        limpiar_campos(sede_entry, numero_contacto_entry, identificador_entry)

    else:
        messagebox.showerror("Error", "No se pudo crear el centro de acopio")

def limpiar_campos(sede_entry, numero_contacto_entry, identificador_entry):
    sede_entry.delete(0, tk.END)
    numero_contacto_entry.delete(0, tk.END)
    identificador_entry.delete(0, tk.END)