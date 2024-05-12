from tkinter import messagebox
import tkinter as tk
from catalogo_materiales import CatalogoMaterialesReciclaje

def crear_material(nombre,unidad,valor,descripcion):
    if CatalogoMaterialesReciclaje().validacion_input_material(nombre,unidad,valor,descripcion):
        CatalogoMaterialesReciclaje().crear_material_reciclaje(nombre,unidad,valor,descripcion)
        messagebox.showinfo("Éxito", "Material creado exitosamente")

def actualizar_lista(lista_text):
    lista_text.delete("1.0", tk.END)
    for material in CatalogoMaterialesReciclaje().materiales:
        lista_text.insert(tk.END, f"{material}\n")