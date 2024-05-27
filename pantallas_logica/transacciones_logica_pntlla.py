import tkinter as tk
from tkinter import messagebox
from catalogo_materiales import CatalogoMaterialesReciclaje
from pantallas_logica.Verifica_Carnet import verifica_usuario_exise
from gestion_transacciones import Transacciones

transaccion = Transacciones()
catalogo_materiales = CatalogoMaterialesReciclaje()

def crear_transaccion(carnet_Entry,centro_combobox,total_tec_colones_Entry):
    # Obtener los datos ingresados por el usuario
    numero_carnet = carnet_Entry.get()
    centro_acopio = centro_combobox.get()
    total_tec_colones = total_tec_colones_Entry.get()

    # Crear una instancia de la clase Transaccion
    if verifica_usuario_exise(numero_carnet):
        transaccion.crear_transaccion(numero_carnet,centro_acopio,total_tec_colones)
    else:
        messagebox.showerror("Error","El usuario no se encuentra en Cuenta Tec")

def obtener_valores_combobox():
    # Obtener la lista de materiales y sus valores del catálogo
    lista_materiales = catalogo_materiales.obtener_lista_materiales()

    # Crear una lista de cadenas con el formato "nombre, valor unitario"
    valores_combobox = [f"{material['nombre']}, {material['valor_unitario']}" for material in lista_materiales]

    return valores_combobox
    

def agregar_material_transaccion(material_combobox, cantidad_Entry, materiales_ag,total_tec_colones_Entry):
    # Obtener el valor seleccionado en el Combobox y dividirlo para obtener el nombre del material y el valor unitario
    material_seleccionado = material_combobox.get()
    nombre_material, valor_unitario = material_seleccionado.split(', ')
    valor_unitario = float(valor_unitario)  # Convertir el valor unitario a número
    
    # Obtener la cantidad de material ingresada
    cantidad_material = int(cantidad_Entry.get())

    # Agregar el material a la transacción
    transaccion.agregar_material(nombre_material, cantidad_material)

    # Calcular el valor total para este material
    valor_total = cantidad_material * valor_unitario

    # Actualizar la vista de materiales agregados
    materiales_ag.insert("", tk.END, values=(nombre_material, valor_total))

    
    total_actual = float(total_tec_colones_Entry.get())
    total_actual += valor_total
    total_tec_colones_Entry.config(state=tk.NORMAL)
    total_tec_colones_Entry.delete(0, tk.END)
    total_tec_colones_Entry.insert(0, f"{total_actual:.2f}")
    total_tec_colones_Entry.config(state=tk.DISABLED)



def continuar_click(carnet_Entry,centro_combobox,total_tec_colones_Entry):
    # Mostrar un cuadro de diálogo de confirmación
    respuesta = messagebox.askyesno("Confirmar transacción", "¿Está seguro de que desea realizar la transacción?")

    # Verificar la respuesta del usuario
    if respuesta:
        # Si el usuario hizo clic en "Sí", crear la transacción
        crear_transaccion(carnet_Entry,centro_combobox,total_tec_colones_Entry)
        messagebox.showinfo("Transacción realizada", "La transacción se ha realizado con éxito.")
    else:
        # Si el usuario hizo clic en "No" o cerró el cuadro de diálogo, no hacer nada
        pass
