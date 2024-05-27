

def guardar_transaccion_base_datos(transaccion):
    with open("./base_datos/transacciones.txt", "a") as file:
        materiales_str = ", ".join([f"{material}:{cantidad}" for material, cantidad in transaccion['materiales'].items()])
        linea = f"{transaccion['numero_carnet']}|{transaccion['centro_acopio']}|{materiales_str}|{transaccion['TecColones']}\n"
        file.write(linea)
