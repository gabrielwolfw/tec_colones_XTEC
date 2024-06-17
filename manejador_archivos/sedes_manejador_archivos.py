
SEDES_ARCHIVO = "./base_datos/sedes.txt"

def guardar_sede_base_datos(sede):
    with open(SEDES_ARCHIVO, 'a') as file:
        sede_str = f"{sede['Nombre']}|{sede['Ubicación']}|{sede['Número de contacto']}|{sede['Estado']}\n"
        file.write(sede_str)

def cargar_sedes_desde_archivo():
    sedes = []
    with open(SEDES_ARCHIVO, "r") as file:
        for linea in file:
            datos = linea.strip().split("|")
            nombre_sede = datos[0]  # Tomar el primer dato como el nombre de la sede
            sedes.append(nombre_sede)
    return sedes