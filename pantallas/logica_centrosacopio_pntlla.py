from tkinter import messagebox
from administacion_sedes import CentrosAcopio


def crear_centro_acopio(sede, numero_contacto, identificador):
    if CentrosAcopio().validar_input_centro_acopio(sede, numero_contacto, identificador):
        CentrosAcopio().crear_centro_acopio(sede, numero_contacto, identificador)
        messagebox.showinfo("Éxito", "Centro de acopio creado exitosamente")
    else:
        messagebox.showerror("Error", "No se pudo crear el centro de acopio")