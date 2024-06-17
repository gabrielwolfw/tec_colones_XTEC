from tkinter import messagebox
import tkinter as tk


def iniciar_sesion(correo_entry, contrasena_entry, auth_frame, root):
    try:
        from pantallas.pantalla_menu import mostrar_pantalla_admin, mostrar_pantalla_encargado, \
            mostrar_pantalla_estudiante
    except ImportError as e:
        messagebox.showerror("Error", f"Error al importar módulos: {e}")
        return

    try:
        correo = correo_entry.get()
        contrasena = contrasena_entry.get()

        if correo == "admin@tec.ac.cr" and contrasena == "1234abcd":
            auth_frame.destroy()
            mostrar_pantalla_admin(root)
        elif correo == "centro@tec.ac.cr" and contrasena == "9900abcd":
            auth_frame.destroy()
            mostrar_pantalla_encargado(root)
        elif correo == "estudiante@tec.ac.cr" and contrasena == "56789abcd":
            auth_frame.destroy()
            mostrar_pantalla_estudiante(root)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error al iniciar sesión: {e}")


def cerrar_sesion(root):
    try:
        from pantallas.autenticacion_pntlla import autenticacion_pantalla
        autenticacion_pantalla(root)
    except ImportError as e:
        messagebox.showerror("Error", f"Error al importar módulos: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error al cerrar sesión: {e}")
