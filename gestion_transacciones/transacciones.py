import datetime
from manejador_archivos import guardar_transaccion_base_datos,gur
from catalogo_materiales import CatalogoMaterialesReciclaje
from Utilidades import generador_identificador

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
    
    def crear_transaccion(self,numero_carnet,centro_acopio,total_tec_colones_Entry):
        tipo = "Aprobada"
        fecha = datetime.datetime.now().strftime("%m/%d/%Y")
        transaccion = {
            "Fecha": fecha,
            "centro_acopio": centro_acopio,
            "materiales": self.materiales,
            "Tipo": tipo
        }
        Estudiante = {
            "numero_carnet": numero_carnet,
            "TecColones": total_tec_colones_Entry,
        }
        self.historial.append(transaccion)
        identificador_unico_transaccion = generador_identificador()
        transaccion['Identificador'] = f"R-{identificador_unico_transaccion}"
        guardar_transaccion_base_datos(transaccion)
        identificador_unico_estudiante = generador_identificador()
        Estudiante['Identificador'] = f"T-{identificador_unico_estudiante}"
        
        self.materiales = {} # Limpiar los materiales después de guardar la transacción




        
