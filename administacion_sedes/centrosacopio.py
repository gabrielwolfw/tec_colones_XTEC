from tkinter import messagebox

class CentrosAcopio:
    def __init__(self):
        self.centros_acopio = []
        self.sedes_existentes = set()
        self.identificadores_existentes = set()
        self.cargar_sedes_desde_archivo()
    
    #
    def validar_input_centro_acopio(self, sede, numero_contacto, identificador):
        try:
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
        except ValueError:
            messagebox.showerror("Error", "El número de contacto debe ser un valor numérico válido.")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {str(e)}")
            return False
    
    def crear_centro_acopio(self, sede, numero_contacto, identificador):
        centro_acopio = {
            "Sede": sede,
            "Número de contacto": numero_contacto,
            "Identificador": identificador
        }
        self.agregar_centro_acopio(centro_acopio)
        self.guardar_centro_acopio_base_datos()
        return True
    
    def agregar_centro_acopio(self, centro_acopio):
        self.centros_acopio.append(centro_acopio)
        return True
    
    # separara la parte de almacenamiento de la parte de logica
    def guardar_centro_acopio_base_datos(self):
        try:
            with open('./base_datos/centrosacopio.txt', 'a') as file:
                for centro_acopio in self.centros_acopio:
                    centro_acopio_str = f"{centro_acopio['Sede']}|{centro_acopio['Número de contacto']}|{centro_acopio['Identificador']}\n"
                    file.write(centro_acopio_str)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al guardar en la base de datos: {str(e)}")
    
    def cargar_sedes_desde_archivo(self):
        try:
            with open('./base_datos/sedes.txt', 'r') as file:
                for line in file:
                    partes = line.strip().split('|')
                    nombre = partes[0]
                    self.sedes_existentes.add(nombre)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al cargar las sedes desde el archivo: {str(e)}")