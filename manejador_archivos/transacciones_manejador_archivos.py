import os
from tkinter import messagebox

TRANSACCIONES_ESTADO_ARCHIVO = "./base_datos/transacciones_estado.txt"
TRANSACCIONES_ARCHIVO = "./base_datos/transacciones.txt"

def guardar_transaccion_base_datos(transaccion):
    with open(TRANSACCIONES_ARCHIVO, "a") as file:
        materiales_str = ", ".join([f"{material}:{cantidad}" for material, cantidad in transaccion['materiales'].items()])
        linea = f"{transaccion['Fecha']}|{transaccion['Sede']}|{transaccion['centro_acopio']}|{materiales_str}|{transaccion['Tipo']}|{transaccion['Identificador']}\n"
        file.write(linea)
    
def guardar_transaccion_anulada_base_datos(transaccion):
    with open(TRANSACCIONES_ARCHIVO, "a") as file:
        linea = f"{transaccion['Fecha']}|{transaccion['Sede']}|{transaccion['centro_acopio']}|{transaccion['materiales']}|{transaccion['Tipo']}|{transaccion['Identificador']}\n"
        file.write(linea)

def leer_datos_de_transacciones():
    with open(TRANSACCIONES_ARCHIVO, "r") as archivo:
        datos = []
        for linea in archivo.readlines():
            transaccion = linea.strip().split("|")
            fecha = transaccion[0] if len(transaccion) > 0 and transaccion[0] else "no está el dato"
            sede = transaccion[1] if len(transaccion) > 1 and transaccion[1] else "no está el dato"
            centro_acopio = transaccion[2] if len(transaccion) > 2 and transaccion[2] else "no está el dato"
            material = transaccion[3] if len(transaccion) > 3 and transaccion[3] else "no está el dato"
            tipo = transaccion[4] if len(transaccion) > 4 and transaccion[4] else "no está el dato"
            identificador=transaccion[5] if len(transaccion) > 5 and transaccion[5] else "no está el dato"
            datos.append((fecha, sede, centro_acopio, material, tipo, identificador))
    return datos


def cargar_transacciones_estado():
    transacciones_estado = {}
    try:
        with open(TRANSACCIONES_ESTADO_ARCHIVO, "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 3:
                    transaccion_id, estado = parts
                    transacciones_estado[transaccion_id] = estado
                else:
                    # Handle the case where the line doesn't split into exactly two parts
                    print(f"Error: línea no válida en el archivo: {line}")

    except FileNotFoundError:
        pass
    print(transacciones_estado)
    return transacciones_estado

def guardar_transacciones_estado(identificador_t):
    with open(TRANSACCIONES_ESTADO_ARCHIVO, "a") as file:
        file.write(f"{identificador_t}\n")


def verificar_transaccion_anulada(identificador_t):
    if os.path.exists(TRANSACCIONES_ESTADO_ARCHIVO):
        with open(TRANSACCIONES_ESTADO_ARCHIVO, "r") as file:
            for line in file:
                if line.strip() == identificador_t:
                    return True  # La transacción ha sido anulada anteriormente
    return False  # La transacción no ha sido anulada anteriormente o el archivo no existe