from tkinter import messagebox
import tkinter as tk

def iniciar_sesion(correo_entry, contrasena_entry, auth_frame, root):
    from pantallas.pantalla_menu import mostrar_pantalla_admin, mostrar_pantalla_encargado, mostrar_pantalla_estudiante
    correo = correo_entry.get()
    contrasena = contrasena_entry.get()
    # Aquí deberías agregar la lógica de autenticación real
    if correo == "admin" and contrasena == "password":  # Ejemplo de autenticación
        auth_frame.destroy()
        mostrar_pantalla_admin(root)
    elif correo == "encargado" and contrasena == "password":  # Ejemplo de autenticación
        auth_frame.destroy()
        mostrar_pantalla_encargado(root)
    elif correo == "estudiante" and contrasena == "password":
        auth_frame.destroy()
        mostrar_pantalla_estudiante(root)
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

def cerrar_sesion(root):
    from pantallas.autenticacion_pntlla import autenticacion_pantalla
    autenticacion_pantalla(root)