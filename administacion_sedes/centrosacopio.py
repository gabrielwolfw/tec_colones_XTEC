from tkinter import messagebox

class CentrosAcopio:
    def __init__(self):
        self.centros_acopio = []
        self.sedes_existentes = set()
        self.identificadores_existentes = set()
        self.centros_acopio_existentes = set()
        self.cargar_sedes_desde_archivo()
        self.cargar_centros_acopio_desde_archivo()

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
        self.sedes_existentes.add(centro_acopio["Sede"])
        self.identificadores_existentes.add(centro_acopio["Identificador"])
        return True

    def guardar_centro_acopio_base_datos(self):
        try:
            with open('./base_datos/centrosacopio.txt', 'a') as file:
                for centro_acopio in self.centros_acopio:
                    centro_acopio_tupla = tuple(centro_acopio.items())
                    if centro_acopio_tupla not in self.centros_acopio_existentes:
                        centro_acopio_str = f"{centro_acopio['Sede']}|{centro_acopio['Número de contacto']}|{centro_acopio['Identificador']}\n"
                        file.write(centro_acopio_str)
                        self.centros_acopio_existentes.add(centro_acopio_tupla)
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

    def cargar_centros_acopio_desde_archivo(self):
        try:
            with open('./base_datos/centrosacopio.txt', 'r') as file:
                for line in file:
                    partes = line.strip().split('|')
                    if len(partes) == 3:
                        sede, numero_contacto, identificador = partes
                        centro_acopio = {
                            "Sede": sede,
                            "Número de contacto": numero_contacto,
                            "Identificador": identificador
                        }
                        self.centros_acopio.append(centro_acopio)
                        self.sedes_existentes.add(sede)
                        self.identificadores_existentes.add(identificador)
                        self.centros_acopio_existentes.add(tuple(centro_acopio.items()))
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al cargar los centros de acopio desde el archivo: {str(e)}")