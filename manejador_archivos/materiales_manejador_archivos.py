
MATERIALES_ARCHIVO = "./base_datos/materiales.txt"

def guardar_material_base_datos(material):
    with open(MATERIALES_ARCHIVO, 'a') as file:
        material_str = f"{material['Identificador']}|{material['Material']}|{material['Unidad']}|{material['Valor unitario']}|{material['Estado']}|{material['Fecha de creacion']}|{material['Descripcion']}\n"
        file.write(material_str)


def cargar_materiales_desde_base_datos():
    materiales = []
    with open(MATERIALES_ARCHIVO, 'r') as file:
        for line in file:
            datos = line.strip().split('|')
            if len(datos) >= 4:  # Asegurar que hay al menos dos elementos
                nombreMaterial = datos[1] # Corregir la codificación
                valorUnitario = datos[3]
                material = {
                    "Material": nombreMaterial,
                    "Valor unitario": valorUnitario
                }
                materiales.append(material)

    return materiales
