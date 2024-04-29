import tkinter as tk
from tkinter import ttk, messagebox

import CatalogoMateriales 


'''
Función para manejar el botón "Crear"
'''
def crear_material():
    nombre = nombre_entry.get()
    unidad = unidad_combobox.get()
    valor = valor_entry.get()
    descripcion = descripcion_text.get("1.0", tk.END)

    if valor.isdigit():
        valor = int(valor)
        if catalogo.crear_material_reciclaje(nombre, unidad, valor, descripcion):
            actualizar_lista()
            messagebox.showinfo("Éxito", "Material creado exitosamente")
    else:
        messagebox.showerror("Error", "El valor unitario debe ser un número entero")

'''
 Función para actualizar la lista de materiales
'''
def actualizar_lista():
    lista_text.delete("1.0", tk.END)
    for material in catalogo.materiales:
        lista_text.insert(tk.END, f"{material} \n")




if __name__ == "__main__": 
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Catalogo de Materiales de Reciclaje")

    # Crear el objeto CatalogoMaterialesReciclaje
    catalogo = CatalogoMateriales.CatalogoMaterialesReciclaje()


    # Crear y posicionar los elementos en la ventana
    nombre_label = tk.Label(root, text="Nombre del material:")
    nombre_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    nombre_entry = tk.Entry(root)
    nombre_entry.grid(row=0, column=1, padx=5, pady=5)

    unidad_label = tk.Label(root, text="Unidad:")
    unidad_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    unidad_combobox = tk.ttk.Combobox(root, values=["kilogramo", "litro", "unidad"])
    unidad_combobox.grid(row=1, column=1, padx=5, pady=5)
    unidad_combobox.current(0)

    valor_label = tk.Label(root, text="Valor Unitario:")
    valor_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    valor_entry = tk.Entry(root)
    valor_entry.grid(row=2, column=1, padx=5, pady=5)

    descripcion_label = tk.Label(root, text="Descripción:")
    descripcion_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    descripcion_text = tk.Text(root, height=4, width=30)
    descripcion_text.grid(row=3, column=1, padx=5, pady=5)

    crear_button = tk.Button(root, text="Crear", command=crear_material)
    crear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    lista_label = tk.Label(root, text="Lista de materiales:")
    lista_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    lista_text = tk.Text(root, height=10, width=200)
    lista_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


    # Actualizar la lista inicial
    actualizar_lista()

    root.mainloop()
