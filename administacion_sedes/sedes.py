from tkinter import messagebox
from manejador_archivos import guardar_sede_base_datos

class Sedes:
    def __init__(self):
        self.sedes = []
        self.identificadores_existentes = set()

    def crear_sede(self, nombre, ubicacion, numero_contacto, estado):
        self.sedes = []
        sede = {
            "Nombre": nombre,
            "Ubicación": ubicacion,
            "Número de contacto": numero_contacto,
            "Estado": estado
        }
        self.agregar_sede(sede)
        guardar_sede_base_datos(sede)
        return True
    
    def agregar_sede(self, sede):
        self.sedes.append(sede)
        return True
    
