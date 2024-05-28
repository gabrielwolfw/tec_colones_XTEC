
import tkinter as tk

from pantallas.mostrar_detalles_pantlla import mostrar_detalles
import datetime


transacción_seleccionada = None
def ingresa_datos_transacciones(transacciones_tree,columnas,datos):
    for col in columnas:
        transacciones_tree.heading(col, text=col)
        transacciones_tree.column(col, width=100)
    for fecha ,carnet, sede, material, costo, tipo  in datos:
        transacciones_tree.insert("", tk.END, values=(fecha, carnet, sede, material, costo, tipo))   

def buscar_transacciones(transacciones_tree,fecha_inicio_entry,fecha_final_entry,centro_acopio_combobox,datos):
    fecha_inicio = fecha_inicio_entry.get_date()
    fecha_final = fecha_final_entry.get_date()
    centro_acopio_seleccionado = centro_acopio_combobox.get()

    # Limpiar tabla de transacciones
    for item in transacciones_tree.get_children():
        transacciones_tree.delete(item)

    # Filtrar transacciones por fecha y centro de acopio
    for transaccion in datos:
        trans_fecha = datetime.datetime.strptime(transaccion[0], "%m/%d/%Y").date()
        trans_centro_acopio = transaccion[2]
        if fecha_inicio <= trans_fecha <= fecha_final and trans_centro_acopio == centro_acopio_seleccionado:
            transacciones_tree.insert("", tk.END, values=transaccion)

def abrir_mostrar_detalles(transacciones_tree,transaccion_frame):
    transaccion_seleccionada = transacciones_tree.focus()
    if transaccion_seleccionada:
        valores = transacciones_tree.item(transaccion_seleccionada)['values']
        fecha, carnet_estudiante, cantidad_material, centro_acopio, tec_colones, tipo = valores
        mostrar_detalles(fecha, carnet_estudiante, cantidad_material, centro_acopio, tec_colones, tipo,transaccion_frame)

def close_window(root, transaccion_frame):
    # Mostrar nuevamente la ventana principal
    root.deiconify()
    transaccion_frame.destroy()

