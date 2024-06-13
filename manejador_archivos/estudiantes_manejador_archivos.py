import os
from tkinter import messagebox

def guardar_Estudiantes_base_datos(estudiante):
    with open("./base_datos/Estudiantes.txt", "a") as file:
            linea = f"{estudiante['numero_carnet']}|{estudiante['TecColones']}|{estudiante['Identificador']}\n"
            file.write(linea)
    

def leer_datos_de_Estudiantes():
    with open("base_datos/Estudiantes.txt", "r") as archivo:
        datos = []
        for linea in archivo.readlines():
            transaccion = linea.strip().split("|")
            carnet = transaccion[0] if len(transaccion) > 0 and transaccion[0] else "no está el dato"
            costo = transaccion[1] if len(transaccion) > 1 and transaccion[1] else "no está el dato"
            identificador = transaccion[2] if len(transaccion) > 2 and transaccion[2] else "no está el dato"
            datos.append((carnet, costo, identificador))
    return datos