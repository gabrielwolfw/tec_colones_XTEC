import tkinter as tk
from tkinter import messagebox
import pantallas.logica_sedes_pntlla as logica_sedes_pntlla

def sedes_pantalla(root):
    # Ocultar la ventana principal
    root.withdraw()
    sede_frame = tk.Toplevel(root)
    sede_frame.title("Administración de Sedes")
    sede_frame.geometry("400x400")
    sede_frame.resizable(False, False)
    sede_frame.configure(bg="#F1F6F9")

    def close_window():
        # Mostrar nuevamente la ventana principal
        root.deiconify()
        sede_frame.destroy()

    sede_frame.protocol("WM_DELETE_WINDOW", close_window)

    nombre_label = tk.Label(sede_frame, text="Nombre de la sede:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    nombre_label.place(x=20, y=20)
    nombre_entry = tk.Entry(sede_frame, width=30)
    nombre_entry.place(x=200, y=20)

    ubicacion_label = tk.Label(sede_frame, text="Ubicación (provincia):", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    ubicacion_label.place(x=20, y=70)
    ubicacion_entry = tk.ttk.Combobox(sede_frame, values=["Cartago", "San José", "Alajuela","Limón","Puntarenas","Heredia","Guanacaste"], font=("Bahnschrift Condensed", 14))
    ubicacion_entry.place(x=200, y=70)

    numero_contacto_label = tk.Label(sede_frame, text="Número de contacto:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    numero_contacto_label.place(x=20, y=120)
    numero_contacto_entry = tk.Entry(sede_frame, width=30)
    numero_contacto_entry.place(x=200, y=120)

    estado_label = tk.Label(sede_frame, text="Estado (activo/inactivo):", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    estado_label.place(x=20, y=170)
    estado_var = tk.StringVar()
    estado_var.set("activo")
    estado_option = tk.OptionMenu(sede_frame, estado_var, "activo", "inactivo")
    estado_option.place(x=200, y=170)

    
    # Crear botón para crear sede
    create_button = tk.Button(sede_frame, text="Crear Sede", command=lambda: logica_sedes_pntlla.crear_sede(
        nombre_entry, ubicacion_entry, numero_contacto_entry, estado_var), font=("Bahnschrift Condensed", 14))
    create_button.place(x=150, y=220)
