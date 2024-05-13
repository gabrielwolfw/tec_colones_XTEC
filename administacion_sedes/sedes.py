from tkinter import messagebox

class Sedes:
    def __init__(self):
        self.sedes = []
        self.identificadores_existentes = set()


    def validar_input_sede(self, nombre, ubicacion, numero_contacto):
        try:
            if not 1 <= len(nombre) <= 50:
                messagebox.showerror("Error", "El nombre de la sede debe tener entre 5 y 50 caracteres")
                return False

            if not 5 <= len(ubicacion) <= 50:
                messagebox.showerror("Error", "La ubicación debe tener entre 5 y 50 caracteres")
                return False

            if not numero_contacto.isdigit() or not 1000000 < int(numero_contacto) < 100000000:
                messagebox.showerror("Error", "El número de contacto debe tener 8 dígitos")
                return False
            return True
        except ValueError:
            messagebox.showerror("Error", "El número de contacto debe ser un valor numérico válido.")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {str(e)}")
            return False


    def crear_sede(self, nombre, ubicacion, numero_contacto, estado):
        self.validar_input_sede(nombre, ubicacion, numero_contacto)
        sede = {
            "Nombre": nombre,
            "Ubicación": ubicacion,
            "Número de contacto": numero_contacto,
            "Estado": estado
        }
        self.agregar_sede(sede)
        return True
    
    def agregar_sede(self, sede):
        self.sedes.append(sede)
        return True