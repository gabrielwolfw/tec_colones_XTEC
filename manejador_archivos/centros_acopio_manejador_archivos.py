
from tkinter import messagebox

CENTROACOPIO_ARCHIVO = "./base_datos/centrosacopio.txt"

def guardar_centro_acopio_base_datos(centro_acopio):
    with open(CENTROACOPIO_ARCHIVO, "a") as file:
        linea = f"{centro_acopio['Sede']}|{centro_acopio['Número de contacto']}|{centro_acopio['Identificador']}\n"
        file.write(linea)

def cargar_centros_acopio_desde_archivo():
    centros_acopio = []
    with open(CENTROACOPIO_ARCHIVO, "r") as file:
        for linea in file:
            sede, numero_contacto, identificador = linea.strip().split("|")
            centros_acopio.append({
                "Sede": sede,
                "Número de contacto": numero_contacto,
                "Identificador": identificador
            })
    return centros_acopio
def cargar_sede_y_centro_acopio_desde_archivo():
    centros_acopio_y_sede = []
    with open("./base_datos/centrosacopio.txt", "r") as file:
        for linea in file:
            elementos = linea.strip().split("|")
            sede = elementos[0]
            identificador = elementos[2]
            centros_acopio_y_sede.append((sede, identificador))
        return centros_acopio_y_sede

