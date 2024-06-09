import os

def validar_existencia_archivo_transacciones():
    return os.path.exists("./base_datos/transacciones.txt")

def validar_existencia_archivo_centros_acopio():
    return os.path.exists("./base_datos/centrosacopio.txt")

def validar_existencia_archivo_materiales():
    return os.path.exists("./base_datos/materiales.txt")

def validar_existencia_archivo_sedes():
    return os.path.exists("./base_datos/sedes.txt")