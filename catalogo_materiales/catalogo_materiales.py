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
    def crear_material_reciclaje(self, nombreMaterial, unidad, valorUnitario, descripcion):
        estado = "Activo"
        fechaCreacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        material = {
            "Material": nombreMaterial,
            "Unidad": unidad,
            "Valor unitario": valorUnitario,
            "Estado": estado,
            "Fecha de creacion": fechaCreacion,
            "Descripcion": descripcion
        }
        self.agregar_material(material)
        self.guardar_material_base_datos()
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

    def guardar_material_base_datos(self):
        try:
            with open('./base_datos/materiales.txt', 'a') as file:
                material = self.materiales[-1]  # Get the last material added
                material_str = f"{material['Identificador']}|{material['Material']}|{material['Unidad']}|{material['Valor unitario']}|{material['Estado']}|{material['Fecha de creacion']}|{material['Descripcion']}\n"
                file.write(material_str)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al guardar en la base de datos: {str(e)}")
        
