import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from pantallas import sedes_pantalla, centrosacopio_panatlla, catalogo_materiales_pantalla, crear_transaccion_pntlla , historial_transacciones 
from pantallas_logica.auten_logica_pntlla import cerrar_sesion

def mostrar_pantalla_admin(root):
    # Mostrar la ventana principal
    root.deiconify()

    crear_button_sede = tk.Button(root, text="Crear sede", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda: sedes_pantalla(root))
    crear_button_sede.place(x=250, y=100)

    crear_button_centroacopio = tk.Button(root, text="Crear centro de acopio", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda: centrosacopio_panatlla(root))
    crear_button_centroacopio.place(x=250, y=150)

    crear_button_historial_ca = tk.Button(root, text="Historial de transacciones", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda: historial_transacciones(root, mostrar_detalles=False,mostrar_centro_acopio=False))
    crear_button_historial_ca.place(x=250, y=200)
    
    cerrar_sesion_button = tk.Button(root, text="Cerrar Sesión", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda:cerrar_sesion(root))
    cerrar_sesion_button.place(x=250, y=250)
    
def mostrar_pantalla_encargado(root):
    # Mostrar la ventana principal
    root.deiconify()
    
    crear_button_catalogomateriales = tk.Button(root, text="Crear material", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda: catalogo_materiales_pantalla(root))
    crear_button_catalogomateriales.place(x=250, y=50)

    crear_button_transaccion = tk.Button(root, text="Crear transacción", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda: crear_transaccion_pntlla(root))
    crear_button_transaccion.place(x=250, y=100)

    crear_button_historial_ca = tk.Button(root, text="Historial de transacciones", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda: historial_transacciones(root,mostrar_detalles=True,mostrar_centro_acopio=True))
    crear_button_historial_ca.place(x=250, y=150)
    
    cerrar_sesion_button = tk.Button(root, text="Cerrar Sesión", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda:cerrar_sesion(root))
    cerrar_sesion_button.place(x=250, y=200)
    
def mostrar_pantalla_estudiante(root):
    # Mostrar la ventana principal
    root.deiconify()
    
    label = tk.Label(root, text="Esta función será implementada\n en un futuro!", font=("Bahnschrift Condensed", 30))
    label.place(x=100, y=150)