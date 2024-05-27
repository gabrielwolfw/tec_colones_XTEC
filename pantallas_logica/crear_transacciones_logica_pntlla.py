import tkinter as tk
from tkinter import messagebox

from administacion_sedes import CentrosAcopio
from catalogo_materiales import CatalogoMaterialesReciclaje
from pantallas_logica.Verifica_Carnet import verifica_usuario_exise
from gestion_transacciones import Transacciones


transaccion = Transacciones()
catalogo_materiales = CatalogoMaterialesReciclaje()
centro_acopio = CentrosAcopio()

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


def agregar_material_transaccion(material_combobox, cantidad_Entry, materiales_ag,total_tec_colones_Entry):
    if not validar_ingreso_datos_agregar_material(material_combobox, cantidad_Entry):
        return
    
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

    limpiar_campos_agregar_material(material_combobox, cantidad_Entry)


def obtener_materiales_combobox():
    # Obtener la lista de materiales y sus valores del catálogo
    lista_materiales = catalogo_materiales.obtener_lista_materiales()

    # Crear una lista de cadenas con el formato "nombre, valor unitario"
    valores_materailes = [f"{material['nombre']}, {material['valor_unitario']}" for material in lista_materiales]

    return valores_materailes
    
def obtener_centros_acopio_combobox():
    lista_centros_acopio = centro_acopio.obtener_identificadores()

    valores_centros_acopio = [f"{centro}" for centro in lista_centros_acopio]
    return valores_centros_acopio



def continuar_click(carnet_Entry, centro_combobox, total_tec_colones_Entry, cantidad_Entry, materiales_ag):
    # Verificar la validez de los datos de ingreso antes de proceder
    if not validar_ingreso_datos_crear_transaccion(carnet_Entry, centro_combobox):
        return

    respuesta = messagebox.askyesno("Confirmar transacción", "¿Está seguro de que desea realizar la transacción?")
    
    if respuesta:
        # Si el usuario hizo clic en "Sí", crear la transacción
        crear_transaccion(carnet_Entry, centro_combobox, total_tec_colones_Entry)
        messagebox.showinfo("Transacción realizada", "La transacción se ha realizado con éxito.")
        limpiar_campos_transaccion(carnet_Entry, centro_combobox, cantidad_Entry, materiales_ag, total_tec_colones_Entry)
    else:
        # Si el usuario hizo clic en "No" o cerró el cuadro de diálogo, no hacer nada
        pass

def validar_ingreso_datos_crear_transaccion(carnet_Entry, centro_combobox):
    if carnet_Entry.get() == "":
        messagebox.showerror("Error", "Debe ingresar un número de carné.")
        return False
    if centro_combobox.get() == "":
        messagebox.showerror("Error", "Debe seleccionar un centro de acopio.")
        return False
    return True

def validar_ingreso_datos_agregar_material(material_combobox, cantidad_Entry):
    if material_combobox.get() == "":
        messagebox.showerror("Error", "Debe seleccionar un material.")
        return False
    if cantidad_Entry.get() == "":
        messagebox.showerror("Error", "Debe ingresar una cantidad.")
        return False
    if not cantidad_Entry.get().isdigit():
        messagebox.showerror("Error", "La cantidad debe ser un número entero.")
        return False
    return True

def limpiar_campos_transaccion(carnet_Entry, centro_combobox, cantidad_Entry, materiales_ag, total_tec_colones_Entry):
    carnet_Entry.delete(0, tk.END)
    centro_combobox.set("")
    cantidad_Entry.delete(0, tk.END)
    materiales_ag.delete(*materiales_ag.get_children())
    total_tec_colones_Entry.config(state=tk.NORMAL)
    total_tec_colones_Entry.delete(0, tk.END)
    total_tec_colones_Entry.insert(0, "0.00")
    total_tec_colones_Entry.config(state=tk.DISABLED)


def limpiar_campos_agregar_material(material_combobox, cantidad_Entry):
    material_combobox.set("")
    cantidad_Entry.delete(0, tk.END)