from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

from administacion_sedes import Sedes


def crear_sede(nombre, ubicacion, numero_contacto, estado):
    if Sedes().validar_input_sede(nombre, ubicacion, numero_contacto):
        Sedes().crear_sede(nombre, ubicacion, numero_contacto, estado)
        messagebox.showinfo("Éxito", "Sede creada exitosamente")
    else:
        messagebox.showerror("Error", "No se pudo crear la sede")



