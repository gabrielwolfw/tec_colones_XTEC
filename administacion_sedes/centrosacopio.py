from tkinter import messagebox

class CentrosAcopio:
    def __init__(self):
        self.centros_acopio = []
        self.identificadores_existentes = set()
    
    def validar_input_centro_acopio(self, nombre, ubicacion, numero_contacto):
        if not 5 <= len(nombre) <= 50:
            messagebox.showerror("Error", "El nombre del centro de acopio debe tener entre 5 y 50 caracteres")
            return False

        if not 5 <= len(ubicacion) <= 50:
            messagebox.showerror("Error", "La ubicación debe tener entre 5 y 50 caracteres")
            return False

        if not numero_contacto.isdigit() or not 0 < int(numero_contacto) < 100000:
            messagebox.showerror("Error", "El número de contacto debe ser un número, y debe de estar entre 1 y 100000")
            return False
        return True
    
    def crear_centro_acopio(self, nombre, ubicacion, numero_contacto, estado):
        self.validar_input_centro_acopio(nombre, ubicacion, numero_contacto)
        centro_acopio = {
            "Nombre": nombre,
            "Ubicación": ubicacion,
            "Número de contacto": numero_contacto,
            "Estado": estado
        }
        self.agregar_centro_acopio(centro_acopio)
        return True
    
    def agregar_centro_acopio(self, centro_acopio):
        self.centros_acopio.append(centro_acopio)
        return True
    
