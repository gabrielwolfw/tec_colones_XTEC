from tkinter import messagebox
import tkinter as tk


from catalogo_materiales.catalogo_materiales import CatalogoMaterialesReciclaje


#Instanacia reutilizable del catalogo de materiales
catalogo_materiales = CatalogoMaterialesReciclaje()

def crear_material(nombre,nombre_entry,unidad,unidad_combobox,valor,valor_entry,descripcion,descripcion_text,lista_text):
    catalogo = CatalogoMaterialesReciclaje()
    if catalogo_materiales.validacion_input_material(nombre,unidad,valor,descripcion):
        catalogo_materiales.crear_material_reciclaje(nombre,unidad,valor,descripcion)
        actualizar_lista(lista_text)
        messagebox.showinfo("Éxito", "Material creado exitosamente")

        # Limpiar las entradas de texto
        nombre_entry.delete(0, tk.END)
        unidad_combobox.set('')
        valor_entry.delete(0, tk.END)
        descripcion_text.delete('1.0', tk.END)
        
    
    else:
        messagebox.showerror("Error", "No se pudo crear el material")

def actualizar_lista(lista_text):
    lista_text.delete("1.0", tk.END)
    for material in catalogo_materiales.materiales:
        lista_text.insert(tk.END, f"Material: {material}\n")

