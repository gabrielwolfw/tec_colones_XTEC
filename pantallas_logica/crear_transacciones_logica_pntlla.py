import tkinter as tk
from tkinter import messagebox
import os

from administacion_sedes import CentrosAcopio
from catalogo_materiales import CatalogoMaterialesReciclaje
from API import validar_carnet
from gestion_transacciones import Transacciones
from manejador_archivos import cargar_centros_acopio_desde_archivo
from manejador_archivos import validar_existencia_archivo_transacciones, validar_existencia_archivo_Estudiantes


transaccion = Transacciones()
catalogo_materiales = CatalogoMaterialesReciclaje()
centro_acopio = CentrosAcopio()

def crear_transaccion(carnet_Entry, centro_combobox, materiales_ag, cantidad_Entry, total_tec_colones_Entry):
    if not validar_existencia_archivo_transacciones():
        messagebox.showerror("Error", "El archivo transacciones.txt no existe, contacte al administrador.")
        return
    if not validar_existencia_archivo_Estudiantes():
        messagebox.showerror("Error", "El archivo estudiantes.txt no existe, contacte al administrador.")
        return

    # Obtener los datos ingresados por el usuario
    numero_carnet = carnet_Entry.get()
    centro_acopio = centro_combobox.get()
    total_tec_colones = total_tec_colones_Entry.get()
    sede = CentrosAcopio.buscar_sede_por_identificador(centro_combobox.get())
    print(sede)
    carnet_valido, status_code, mensaje_detalle = validar_carnet(numero_carnet)


    mensaje = f"{mensaje_detalle} (Código de estado: {status_code})"
    if validar_carnet(numero_carnet)[0]:
        transaccion.crear_transaccion(numero_carnet, sede, centro_acopio, total_tec_colones)
        messagebox.showinfo("Transacción realizada", mensaje)
        limpiar_campos_transaccion(carnet_Entry, centro_combobox, cantidad_Entry, materiales_ag, total_tec_colones_Entry)
    else:
        messagebox.showerror("Error", mensaje)


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
    valores_materiales = [f"{material['Material']}, {material['Valor unitario']}" for material in lista_materiales]

    return valores_materiales
    
def obtener_centros_acopio_combobox():
    centros_acopio_list = centro_acopio.obtener_identificadores()
    return centros_acopio_list



def continuar_click(carnet_Entry, centro_combobox, total_tec_colones_Entry, cantidad_Entry, materiales_ag):

    # Verificar la validez de los datos de ingreso antes de proceder
    if not validar_ingreso_datos_crear_transaccion(centro_combobox, materiales_ag):
        return


    respuesta = messagebox.askyesno("Confirmar transacción", "¿Está seguro de que desea realizar la transacción?")
    
    if respuesta:
        # Si el usuario hizo clic en "Sí", crear la transacción
        crear_transaccion(carnet_Entry, centro_combobox, materiales_ag, cantidad_Entry, total_tec_colones_Entry)
    else:
        # Si el usuario hizo clic en "No" o cerró el cuadro de diálogo, no hacer nada
        pass

def validar_ingreso_datos_crear_transaccion(centro_combobox,materiales_ag):
    if centro_combobox.get() == "":
        messagebox.showerror("Error", "Debe seleccionar un centro de acopio.")
        return False
    if len(materiales_ag.get_children()) == 0:
        messagebox.showerror("Error", "Debe agregar al menos un material.")
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
    cantidad_Entry.delete(0, tk.END)  # Limpiar el widget cantidad_Entry solo si hay algo para eliminar
    if materiales_ag.get_children():  # Verificar si hay elementos para eliminar en el Treeview
        materiales_ag.delete(*materiales_ag.get_children())  # Eliminar los elementos del Treeview
    total_tec_colones_Entry.config(state=tk.NORMAL)
    total_tec_colones_Entry.delete(0, tk.END)
    total_tec_colones_Entry.insert(0, "0.00")
    total_tec_colones_Entry.config(state=tk.DISABLED)


def limpiar_campos_agregar_material(material_combobox, cantidad_Entry):
    material_combobox.set("")
    cantidad_Entry.delete(0, tk.END)

def close_window(root,transaccion_frame):
    # Mostrar nuevamente la ventana principal
    root.deiconify()
    transaccion_frame.destroy()