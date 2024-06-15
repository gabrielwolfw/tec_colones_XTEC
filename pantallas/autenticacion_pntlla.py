import tkinter as tk
from tkinter import messagebox, ttk
import pantallas_logica.auten_logica_pntlla as auten_logica_pntlla
from pantallas.pantalla_menu import mostrar_pantalla_encargado, mostrar_pantalla_admin, mostrar_pantalla_estudiante

def autenticacion_pantalla(root):
    # Ocultar la ventana principal
    root.withdraw()

    auth_frame = tk.Toplevel(root)
    auth_frame.title("Autenticación")
    auth_frame.geometry("300x350")
    auth_frame.resizable(False, False)
    auth_frame.configure(bg="white")

    def close_window(root):
        # Cerrar la ventana principal
        root.destroy()
        # Cerrar la aplicación
        root.quit()

    auth_frame.protocol("WM_DELETE_WINDOW", lambda: close_window(root))

    # Configurar el estilo
    style = ttk.Style()
    style.configure("TLabel", font=("Bahnschrift Condensed", 14), background="white")
    style.configure("TEntry", font=("Bahnschrift Condensed", 14))
    style.configure("TButton", font=("Bahnschrift Condensed", 14), background="#A5C0DD", foreground="white")

    # Título
    titulo_label = tk.Label(auth_frame, text="Iniciar Sesión en Tec-Colones", font=("Bahnschrift Condensed", 16, "bold"), bg="white")
    titulo_label.pack(pady=(20, 10))

    # Correo institucional
    correo_label = ttk.Label(auth_frame, text="Correo institucional:")
    correo_label.pack(pady=(10, 5))
    correo_entry = ttk.Entry(auth_frame, width=30)
    correo_entry.pack()

    # Contraseña
    contrasena_label = ttk.Label(auth_frame, text="Contraseña:")
    contrasena_label.pack(pady=(10, 5))
    contrasena_entry = ttk.Entry(auth_frame, show="*", width=30)
    contrasena_entry.pack()

    # Botón de Iniciar sesión
    iniciar_sesion_button = ttk.Button(auth_frame, text="Iniciar sesión", command=lambda: auten_logica_pntlla.iniciar_sesion(correo_entry, contrasena_entry, auth_frame,root))
    iniciar_sesion_button.pack(pady=(20, 10))

    # Botón de Salir
    salir_button = ttk.Button(auth_frame, text="Salir", command=lambda: close_window(root))
    salir_button.pack(pady=(10, 20))
