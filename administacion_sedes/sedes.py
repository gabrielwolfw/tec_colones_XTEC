from tkinter import messagebox

class Sedes:
    def __init__(self):
        self.sedes = []
        self.identificadores_existentes = set()


    def validar_input_sede(self, nombre, ubicacion, numero_contacto):
        if not 5 <= len(nombre) <= 50:
            messagebox.showerror("Error", "El nombre de la sede debe tener entre 5 y 50 caracteres")
            return False

        if not 5 <= len(ubicacion) <= 50:
            messagebox.showerror("Error", "La ubicación debe tener entre 5 y 50 caracteres")
            return False

        if not numero_contacto.isdigit() or not 0 < int(numero_contacto) < 100000:
            messagebox.showerror("Error", "El número de contacto debe ser un número, y debe de estar entre 1 y 100000")
            return False
        return True


    def crear_sede(self, nombre, ubicacion, numero_contacto, estado):
        self.validar_input_sede(nombre, ubicacion, numero_contacto)
        sede = {
            "Nombre": nombre,
            "Ubicación": ubicacion,
            "Número de contacto": numero_contacto,
            "Estado": estado
        }
        self.agregar_sede(sede)
        return True
    
    def agregar_sede(self, sede):
        self.sedes.append(sede)
        return True