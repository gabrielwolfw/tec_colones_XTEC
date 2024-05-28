from tkinter import messagebox
from manejador_archivos import cargar_centros_acopio_desde_archivo,cargar_sedes_desde_archivo,guardar_centro_acopio_base_datos

class CentrosAcopio:
    def __init__(self):
        self.centros_acopio = []
        self.sedes_existentes = []
        self.identificadores_existentes = []
        self.obtener_sedes()
        self.obtener_identificadores()

    def crear_centro_acopio(self, sede, numero_contacto, identificador):
        centro_acopio = {
            "Sede": sede,
            "Número de contacto": numero_contacto,
            "Identificador": identificador
        }
        self.agregar_centro_acopio(centro_acopio)
        guardar_centro_acopio_base_datos(centro_acopio)
        return True

    def agregar_centro_acopio(self, centro_acopio):
        self.centros_acopio.append(centro_acopio)
        self.sedes_existentes.append(centro_acopio["Sede"])
        self.identificadores_existentes.append(centro_acopio["Identificador"])
        return True
    
    def obtener_sedes(self):
        sedes = cargar_sedes_desde_archivo()
        self.sedes_existentes = sedes
        return self.sedes_existentes

    
    def obtener_identificadores(self):
        self.identificadores_existentes = []
        centros_acopio = cargar_centros_acopio_desde_archivo()
        for centro in centros_acopio:
            self.identificadores_existentes.append(centro["Identificador"])
        return self.identificadores_existentes







