import os
from tkinter import messagebox

def guardar_transaccion_base_datos(transaccion):
    with open("./base_datos/transacciones.txt", "a") as file:
        materiales_str = ", ".join([f"{material}:{cantidad}" for material, cantidad in transaccion['materiales'].items()])
        linea = f"{transaccion['Fecha']}|{transaccion['centro_acopio']}|{materiales_str}|{transaccion['Tipo']}|{transaccion['Identificador']}\n"
        file.write(linea)
    

def leer_datos_de_transacciones():
    with open("base_datos/transacciones.txt", "r") as archivo:
        datos = []
        for linea in archivo.readlines():
            transaccion = linea.strip().split("|")
            fecha = transaccion[0] if len(transaccion) > 0 and transaccion[0] else "no está el dato"
            sede = transaccion[1] if len(transaccion) > 1 and transaccion[1] else "no está el dato"
            material = transaccion[2] if len(transaccion) > 2 and transaccion[2] else "no está el dato"
            tipo = transaccion[3] if len(transaccion) > 3 and transaccion[3] else "no está el dato"
            identificador=transaccion[4] if len(transaccion) > 4 and transaccion[4] else "no está el dato"
            datos.append((fecha, sede, material,tipo,identificador))
    return datos