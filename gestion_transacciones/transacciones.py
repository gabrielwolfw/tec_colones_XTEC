import datetime

from manejador_archivos import guardar_transaccion_base_datos
from catalogo_materiales import CatalogoMaterialesReciclaje
catalogo_materiales = CatalogoMaterialesReciclaje()

class Transacciones:
    def __init__(self):
        self.materiales = {}
        self.historial= []
    
    def agregar_material(self, material_reciclado,cantidad_material):
        if material_reciclado in self.materiales:
            self.materiales[material_reciclado] += cantidad_material
        else:
            self.materiales[material_reciclado] = cantidad_material
    
    def crear_transaccion(self, numero_carnet, sede, centro_acopio,total_tec_colones_Entry):
        tipo = "Aprobada"
        fecha = datetime.datetime.now().strftime("%m/%d/%Y")
        transaccion = {
            "Fecha": fecha,
            "numero_carnet": numero_carnet,
            "sede": sede,
            "centro_acopio": centro_acopio,
            "materiales": self.materiales,
            "TecColones": total_tec_colones_Entry,
            "Tipo": tipo
        }
        self.historial.append(transaccion)
        guardar_transaccion_base_datos(transaccion)
        self.materiales = {} # Limpiar los materiales después de guardar la transacción
        print(centro_acopio)



        
