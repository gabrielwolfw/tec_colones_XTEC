import datetime

'''
Clase que permite crear materiales de reciclaje
'''
class CatalogoMaterialesReciclaje:
    def __init__(self,materiales):
        self.materiales = materiales
    
    '''
    Metodo que permite crear un material de reciclaje
    '''
    def crear_material_reciclaje(self, nombreMaterial, unidad, valorUnitario, estado,fechaCreacion,descripcion):
        # Restricciones
        if not 5 <= len(nombreMaterial) <= 50:
            return "El nombre del material debe tener entre 5 y 50 caracteres"
        
        if unidad not in ["Kilogramo","litro","Unidad"]:
            return "La unidad del material no es válida"
        
        if valorUnitario >= 0 and valorUnitario <= 100000:
            return "El valor unitario debe ser mayor a 0 y menor a 100000"
        
        if len(descripcion) > 1000:
            return "La descripción del material no puede tener más de 1000 caracteres"
        
        # El estado del material siempre será "Activo" al ser creado
        estado = "Activo"

        # Fecha autogenerada con día y hora actual
        fechaCreacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Crear material
        material = {
            "nombreMaterial": nombreMaterial,
            "unidad": unidad,
            "valorUnitario": valorUnitario,
            "estado": estado,
            "fechaCreacion": fechaCreacion,
            "descripcion": descripcion
        }
        
        # Añade el material a la lista de materiales
        self.materiales.append(material)
        
