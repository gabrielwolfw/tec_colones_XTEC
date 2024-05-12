from tkinter import messagebox

class CentrosAcopio:
    def __init__(self):
        self.centros_acopio = []
        self.sedes_existentes = set()
        self.identificadores_existentes = set()
    
    def validar_input_centro_acopio(self, sede, numero_contacto,identificador):
        if not sede in self.sedes_existentes:
            messagebox.showerror("Error", "La sede no existe")
            return False
        if not numero_contacto.isdigit() or not 1000000 < int(numero_contacto) < 100000000:
            messagebox.showerror("Error", "El número de contacto debe ser un número debe tener 8 dígitos")
            return False
        if identificador in self.identificadores_existentes:
            messagebox.showerror("Error", "El identificador ya existe")
            return False
        return True
    
    def crear_centro_acopio(self, sede, numero_contacto, identificador):
        self.validar_input_centro_acopio(sede, numero_contacto, identificador)
        centro_acopio = {
            "Sede": sede,
            "Número de contacto": numero_contacto,
            "Identificador": identificador
        }
        self.agregar_centro_acopio(centro_acopio)
        return True
    
    def agregar_centro_acopio(self, centro_acopio):
        self.centros_acopio.append(centro_acopio)
        return True
    

    def guardar_centro_acopio_base_datos(self):
        with open('./base_datos/centrosacopio.txt','a') as file:
            for centro_acopio in self.centros_acopio:
                file.write(f"{centro_acopio}\n")
    
