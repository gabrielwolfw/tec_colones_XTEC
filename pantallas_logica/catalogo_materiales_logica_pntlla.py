from tkinter import messagebox
import tkinter as tk


from catalogo_materiales.catalogo_materiales import CatalogoMaterialesReciclaje
from manejador_archivos import validar_existencia_archivo_materiales
#Instanacia reutilizable del catalogo de materiales
catalogo_materiales = CatalogoMaterialesReciclaje()

def crear_material(nombre_entry, unidad_combobox, valor_entry, descripcion_text, lista_text):
    if not validar_existencia_archivo_materiales():
        messagebox.showerror("Error", "No se ha encontrado el archivo de materiales, por favor contacte al administrador.")
        return
    nombre = nombre_entry.get()
    unidad = unidad_combobox.get()
    valor = valor_entry.get()
    descripcion = descripcion_text.get("1.0", tk.END)

    if validacion_input_material(nombre,unidad,valor,descripcion):
        catalogo_materiales.crear_material_reciclaje(nombre,unidad,valor,descripcion)
        actualizar_lista(lista_text)
        messagebox.showinfo("Éxito", "Material creado exitosamente")
        limpiar_campos(nombre_entry, unidad_combobox, valor_entry, descripcion_text)

    else:
        messagebox.showerror("Error", "No se pudo crear el material")

def actualizar_lista(lista_text):
    lista_text.delete("1.0", tk.END)
    for material in catalogo_materiales.materiales:
        lista_text.insert(tk.END, f"Material: {material}\n")

def limpiar_campos(nombre_entry, unidad_combobox, valor_entry, descripcion_text):
    nombre_entry.delete(0, tk.END)
    unidad_combobox.set('')
    valor_entry.delete(0, tk.END)
    descripcion_text.delete('1.0', tk.END)


def validacion_input_material(nombreMaterial, unidad, valorUnitario, descripcion):
    try:
        if not 5 <= len(nombreMaterial) <= 50:
            messagebox.showerror("Error", "El nombre del material debe tener entre 5 y 50 caracteres")
            return False

        if unidad not in ["kilogramo","litro","unidad"]:
            messagebox.showerror("Error", "La unidad del material no es válida")
            return False

        valorUnitario = int(valorUnitario)
        if not 0 < valorUnitario < 100000:
            messagebox.showerror("Error", "El valor unitario debe ser mayor a 0 y menor a 100000")
            return False

        if len(descripcion) > 1000:
            messagebox.showerror("Error", "La descripción del material no puede tener más de 1000 caracteres")
            return False
        return True
    except ValueError:
        messagebox.showerror("Error", "El valor unitario debe ser un valor numérico válido.")
        return False
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {str(e)}")
        return False