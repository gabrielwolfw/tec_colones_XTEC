import datetime
import secrets
import hashlib
from tkinter import messagebox


'''
Clase para manejar el catálogo de materiales de reciclaje
'''
class CatalogoMaterialesReciclaje:
    def __init__(self):
        self.materiales = []
        self.identificadores_existentes = set()


    '''
    Método para crear un material de reciclaje

    Parametros: nombreMaterial (str): Nombre del material
                unidad (str): Unidad del material
                valorUnitario (int): Valor unitario del material en Tec_Colones
                descripcion (str): Descripción del material
    '''
    def validacion_input_material(self, nombreMaterial, unidad, valorUnitario, descripcion):
        if not 5 <= len(nombreMaterial) <= 50:
            messagebox.showerror("Error El nombre del material debe tener entre 5 y 50 caracteres")
            return False
        
        if unidad not in ["kilogramo","litro","unidad"]:
            messagebox.showerror("Error", "La unidad del material no es válida")
            return False
        
        valorUnitario = int(valorUnitario)
        if not 0 < valorUnitario < 100000:
            messagebox.showerror("Error", "El valor unitario debe ser mayor a 0 y menor a 100000")
            return False
        
        if len(descripcion) > 1000:
            messagebox.showerror("Error", "La descripción del material no puede tener más de 1000 caracteres")
            return False
        return True
    
    def crear_material_reciclaje(self, nombreMaterial, unidad, valorUnitario, descripcion):
        estado = "Activo" 
        fechaCreacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        material = {
            "Material": nombreMaterial,
            "Unidad": unidad,
            "Valor unitario": valorUnitario,
            "Estado": estado,
            "Fecha de creación": fechaCreacion,
            "Descripcion": descripcion
        }
        self.agregar_material(material)
        return True
    
    '''
    Método para agregar un material al catálogo

    Paramentros: material (dict): Diccionario con la información del material
    '''
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
        
