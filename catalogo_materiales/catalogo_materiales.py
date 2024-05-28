import datetime
import secrets
import hashlib
from tkinter import messagebox

from manejador_archivos import guardar_material_base_datos, cargar_materiales_desde_base_datos

'''
Clase para manejar el catálogo de materiales de reciclaje
'''
class CatalogoMaterialesReciclaje:
    def __init__(self):
        self.materiales = []
        self.identificadores_existentes = set()
        self.lista_materiales_precio = []
        self.obtener_lista_materiales()
    

    def crear_material_reciclaje(self, nombreMaterial, unidad, valorUnitario, descripcion):
        estado = "Activo"
        fechaCreacion = datetime.datetime.now().strftime("%Y-%m-%d")
        material = {
            "Material": nombreMaterial,
            "Unidad": unidad,
            "Valor unitario": valorUnitario,
            "Estado": estado,
            "Fecha de creacion": fechaCreacion,
            "Descripcion": descripcion
        }
        self.agregar_material(material)
        guardar_material_base_datos(material)
        
    
    def agregar_material(self, material):
        material['Identificador'] = self.generar_identificador_unico()
        self.materiales.append(material)
        self.identificadores_existentes.add(material['Identificador'])

    '''
    Método para mostrar los materiales del catálogo
    '''
    def mostrar_materiales(self):
        print("Lista de materiales:")
        for material in self.materiales:
            print(material)

    '''
    Método para generar un identificador único para un material
    '''
    def generar_identificador_unico(self):
        while True:
            token = secrets.token_hex(6)
            hash_object = hashlib.sha256(token.encode())
            hash_token = hash_object.hexdigest()[:12]
            key_id = f"M-{hash_token}"
            if key_id not in self.identificadores_existentes:
                return key_id
    
    '''
    Obtiene una lista de materiales unicamente con el nombre y valor unitario
    '''
    def obtener_lista_materiales(self):
        lista_materiales = cargar_materiales_desde_base_datos()
        self.lista_materiales_precio = lista_materiales
        return self.lista_materiales_precio


# Crear una instancia de CatalogoMaterialesReciclaje
catalogo = CatalogoMaterialesReciclaje()

# Obtener la lista de materiales con sus valores unitarios
lista_materiales = catalogo.obtener_lista_materiales()
print(lista_materiales)