from tkinter import messagebox
import tkinter as tk
import pantallas.logica_sedes_pntlla as logica_sedes_pntlla

def sedes_pantalla(root):
    sede_frame = tk.Toplevel(root)
    sede_frame.title("Administración de Sedes")
    sede_frame.geometry("400x300")
    sede_frame.resizable(False, False)

    nombre_label = tk.Label(sede_frame, text="Nombre de la sede:")
    nombre_label.pack()
    nombre_entry = tk.Entry(sede_frame, width=30)
    nombre_entry.pack()

    ubicacion_label = tk.Label(sede_frame, text="Ubicación (provincia):")
    ubicacion_label.pack()
    ubicacion_entry = tk.Entry(sede_frame, width=30)
    ubicacion_entry.pack()

    numero_contacto_label = tk.Label(sede_frame, text="Número de contacto:")
    numero_contacto_label.pack()
    numero_contacto_entry = tk.Entry(sede_frame, width=30)
    numero_contacto_entry.pack()

    estado_label = tk.Label(sede_frame, text="Estado (activo/inactivo):")
    estado_label.pack()
    estado_var = tk.StringVar()
    estado_var.set("activo")
    estado_option = tk.OptionMenu(sede_frame, estado_var, "activo", "inactivo")
    estado_option.pack()

    # Create button to create sede
    create_button = tk.Button(sede_frame, text="Crear Sede", command=lambda: logica_sedes_pntlla.crear_sede(
        nombre_entry.get(), ubicacion_entry.get(), numero_contacto_entry.get(), estado_var.get()))
    create_button.pack()





