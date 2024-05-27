from tkinter import messagebox

class Sedes:
    def __init__(self):
        self.sedes = []
        self.identificadores_existentes = set()

    def crear_sede(self, nombre, ubicacion, numero_contacto, estado):
        self.sedes = []
        sede = {
            "Nombre": nombre,
            "Ubicación": ubicacion,
            "Número de contacto": numero_contacto,
            "Estado": estado
        }
        self.agregar_sede(sede)
        self.guardar_sede_base_datos()
        return True
    
    def agregar_sede(self, sede):
        self.sedes.append(sede)
        return True
    
    def guardar_sede_base_datos(self):
        try:
            with open('./base_datos/sedes.txt', 'a') as file:
                for sede in self.sedes:
                    sede_str = f"{sede['Nombre']}|{sede['Ubicación']}|{sede['Número de contacto']}|{sede['Estado']}\n"
                    file.write(sede_str)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al guardar en la base de datos: {str(e)}")