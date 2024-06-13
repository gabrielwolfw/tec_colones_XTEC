import os
from tkinter import messagebox

def guardar_Estudiantes_base_datos(transaccion):
    with open("./base_datos/Estudiantes.txt", "a") as file:
        linea = f"{transaccion['numero_carnet']}|{transaccion['TecColones']}\n"
        file.write(linea)
    

def leer_datos_de_Estudiantes():
    with open("base_datos/Estudiantes.txt", "r") as archivo:
        datos = []
        for linea in archivo.readlines():
            transaccion = linea.strip().split("|")
            carnet = transaccion[0] if len(transaccion) > 0 and transaccion[0] else "no está el dato"
            costo = transaccion[1] if len(transaccion) > 1 and transaccion[1] else "no está el dato"
            datos.append((carnet, costo))
    return datos