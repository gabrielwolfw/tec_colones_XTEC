from tkinter import messagebox
from manejador_archivos import cargar_centros_acopio_desde_archivo,cargar_sedes_desde_archivo,guardar_centro_acopio_base_datos

class CentrosAcopio:
    def __init__(self):
        self.centros_acopio = []
        self.sedes_existentes = set()
        self.identificadores_existentes = set()
        self.centros_acopio_existentes = set()
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        # Cargar sedes desde archivo
        sedes = cargar_sedes_desde_archivo()
        self.sedes_existentes.update(sedes)
        
        # Cargar centros de acopio desde archivo
        centros_acopio = cargar_centros_acopio_desde_archivo()
        self.centros_acopio.extend(centros_acopio)
        for centro in centros_acopio:
            self.sedes_existentes.add(centro["Sede"])
            self.identificadores_existentes.add(centro["Identificador"])

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
        self.sedes_existentes.add(centro_acopio["Sede"])
        self.identificadores_existentes.add(centro_acopio["Identificador"])
        return True
    
    def obtener_sedes(self):
        return list(self.sedes_existentes)

    
    def obtener_identificadores(self):
        return [centro["Identificador"] for centro in self.centros_acopio]




