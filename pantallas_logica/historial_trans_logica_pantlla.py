
import tkinter as tk
from tkinter import messagebox,ttk
from pantallas.mostrar_detalles_pantlla import mostrar_detalles
import datetime



def ingresa_datos_transacciones(transacciones_tree, columnas, datos_t, datos_e):
    for col in columnas:
        transacciones_tree.heading(col, text=col)
        transacciones_tree.column(col, width=100)

    for fecha, sede, material, tipo, identificador_t in datos_t:
        identificador_t_sin_prefijo = identificador_t[2:]  # Suponiendo que identificador_t tiene un prefijo
        for carnet, costo, identificador_e in datos_e:
            identificador_e_sin_prefijo = identificador_e[2:]  # Suponiendo que identificador_e tiene un prefijo
            if identificador_t_sin_prefijo == identificador_e_sin_prefijo:
                transacciones_tree.insert("", tk.END, values=(fecha, sede, material, tipo, carnet, costo))

def buscar_transacciones(fecha_final_entry, fecha_inicio_entry, centro_acopio_combobox, transacciones_tree, datos_e, datos_t):
    try:
        fecha_inicio = fecha_inicio_entry.get_date()
        fecha_final = fecha_final_entry.get_date()
        centro_acopio_seleccionado = centro_acopio_combobox.get()

        # Verificar si las fechas o el centro de acopio están vacíos
        if not fecha_inicio or not fecha_final or not centro_acopio_seleccionado:
            raise ValueError("Las fechas de inicio y fin, y el centro de acopio son obligatorios.")
        
        # Verificar que la fecha final sea mayor o igual a la fecha inicial
        if fecha_inicio > fecha_final:
            messagebox.showerror("Error", "La fecha inicial no puede ser mayor a la fecha final.")
            return
        
        # Limpiar tabla de transacciones
        for item in transacciones_tree.get_children():
            transacciones_tree.delete(item)

        # Filtrar transacciones por fecha y centro de acopio
        filtered_transactions = []
        for fecha, sede, material, tipo, identificador_t in datos_t:
            try:
                trans_fecha = datetime.datetime.strptime(fecha, "%m/%d/%Y").date()
            except ValueError as e:
                # Manejar errores en el formato de fecha de la transacción
                print(f"Error al convertir fecha de la transacción: {e}")
                continue
            trans_centro_acopio = sede
            if fecha_inicio <= trans_fecha <= fecha_final and trans_centro_acopio == centro_acopio_seleccionado:
                # Buscar los datos del estudiante correspondiente
                for carnet, costo, identificador_e in datos_e:
                    identificador_t_sin_prefijo = identificador_t[2:]  # Suponiendo que identificador_t tiene un prefijo
                    identificador_e_sin_prefijo = identificador_e[2:]  # Suponiendo que identificador_e tiene un prefijo
                    if identificador_t_sin_prefijo == identificador_e_sin_prefijo:
                        filtered_transactions.append((fecha, sede, material, tipo, carnet, costo))
                        break  # Salir del bucle una vez encontrado el estudiante

        # Verificar si no se encontraron transacciones
        if not filtered_transactions:
            messagebox.showinfo("Información", "No se encontraron transacciones para los criterios seleccionados.")
        else:
            for transaccion in filtered_transactions:
                transacciones_tree.insert("", tk.END, values=transaccion)

    except ValueError as e:
        # Manejar errores de conversión de fecha, entrada inválida, fechas vacías o centro de acopio vacío
        messagebox.showerror("Error", f"Error al obtener las fechas o el centro de acopio: {e}")
        return

def mostrar_transaccion_detalles(transaccion_frame, transacciones_tree, datos_t, datos_e, transaccion_seleccionada):
    # Obtener la transacción seleccionada
    transaccion_seleccionada = transacciones_tree.focus()
    if transaccion_seleccionada:
        valores = transacciones_tree.item(transaccion_seleccionada)['values']
        if valores:
            fecha, centro_acopio, cantidad_material, tipo, carnet_estudiante, tec_colones = valores
            
            # Obtener identificador_t correspondiente a la transacción seleccionada
            identificador_t = None
            for fecha_t, sede, material_t, tipo_t, identificador_t in datos_t:
                if (fecha_t, sede, material_t, tipo_t) == (fecha, centro_acopio, cantidad_material, tipo):
                    break
            
            if identificador_t:
                mostrar_detalles(fecha, centro_acopio, cantidad_material, tipo, carnet_estudiante, tec_colones, transaccion_frame, identificador_t)
            else:
                messagebox.showwarning("Advertencia", "No se encontró el identificador de la transacción seleccionada.")
        else:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna transacción.")
    else:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna transacción.")

def close_window(root, transaccion_frame):
    # Mostrar nuevamente la ventana principal
    root.deiconify()
    transaccion_frame.destroy()

