import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from tkcalendar import DateEntry
from manejador_archivos.transacciones_manejador_archivos import leer_datos_de_transacciones
import pantallas_logica.crear_transacciones_logica_pntlla as transaccion_logica
from pantallas.mostrar_detalles_pantlla import mostrar_detalles
from manejador_archivos import leer_datos_de_Estudiantes

transacción_seleccionada = None


def historial_transacciones(root):
    # Ocultar la ventana principal
    root.withdraw()

    transaccion_frame = tk.Toplevel(root)
    transaccion_frame.title("Historial de transacciones")
    transaccion_frame.geometry("800x400")
    transaccion_frame.resizable(False, False)

    # Labels y Entradas de búsqueda
    fecha_inicio_label = tk.Label(transaccion_frame, text="Fecha inicio", font=("Bahnschrift Condensed", 12))
    fecha_inicio_label.place(x=20, y=20)
    fecha_inicio_entry = DateEntry(transaccion_frame, width=12, background='darkblue', foreground='white',
                                   borderwidth=2)
    fecha_inicio_entry.place(x=120, y=20)

    fecha_final_label = tk.Label(transaccion_frame, text="Fecha final", font=("Bahnschrift Condensed", 12))
    fecha_final_label.place(x=250, y=20)
    fecha_final_entry = DateEntry(transaccion_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    fecha_final_entry.place(x=340, y=20)

    valores_centros_acopio = transaccion_logica.obtener_centros_acopio_combobox()
    centro_acopio_label = tk.Label(transaccion_frame, text="Centro de acopio", font=("Bahnschrift Condensed", 12))
    centro_acopio_label.place(x=470, y=20)
    centro_acopio_combobox = ttk.Combobox(transaccion_frame, values=valores_centros_acopio,
                                          font=("Bahnschrift Condensed", 12))
    centro_acopio_combobox.place(x=570, y=20)
    centro_acopio_combobox.current(0)

    buscar_button = tk.Button(transaccion_frame, text="Buscar", font=("Bahnschrift Condensed", 12), bg="#A5C0DD",
                              command=lambda: buscar_transacciones())
    buscar_button.place(x=745, y=15)

    # Tabla de transacciones
    columnas = ("Fecha", "Centro de acopio", "Material:Cantidad", "Tipo", "Carnet estudiante", "TecColones",)
    transacciones_tree = ttk.Treeview(transaccion_frame, columns=columnas, show="headings")
    transacciones_tree.place(x=20, y=60, width=760, height=280)

    for col in columnas:
        transacciones_tree.heading(col, text=col)
        transacciones_tree.column(col, width=100)

    datos_t = leer_datos_de_transacciones()
    datos_e = leer_datos_de_Estudiantes()

    for fecha, sede, material, tipo, identificador_t in datos_t:
        identificador_t_sin_prefijo = identificador_t[2:]  
        for carnet, costo, identificador_e in datos_e:
            identificador_e_sin_prefijo = identificador_e[2:] 
            if identificador_t_sin_prefijo == identificador_e_sin_prefijo:
                transacciones_tree.insert("", tk.END, values=(fecha, sede, material, tipo, carnet, costo))
    
        # Botón de Ver Detalles
    ver_detalles_button = tk.Button(transaccion_frame, text="Ver detalles", font=("Bahnschrift Condensed", 12), bg="#A5C0DD",
                                    command=lambda: mostrar_transaccion_detalles())
    ver_detalles_button.place(x=695, y=350)

    # Botón de Salir
    salir_button = tk.Button(transaccion_frame, text="Salir", font=("Bahnschrift Condensed", 12), bg="#A5C0DD",
                             command=lambda: close_window())
    salir_button.place(x=20, y=350)

    def close_window():
        # Mostrar nuevamente la ventana principal
        root.deiconify()
        transaccion_frame.destroy()

    def mostrar_transaccion_detalles():
        # Obtener la transacción seleccionada
        transaccion_seleccionada = transacciones_tree.focus()
        if transaccion_seleccionada:
            valores = transacciones_tree.item(transaccion_seleccionada)['values']
            if valores:
                fecha, centro_acopio, cantidad_material, tipo, carnet_estudiante, tec_colones = valores
                mostrar_detalles(fecha, centro_acopio, cantidad_material, tipo, carnet_estudiante, tec_colones, transaccion_frame)
            else:
                messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna transacción.")
        else:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna transacción.")

    def buscar_transacciones():
        try:
            fecha_inicio = fecha_inicio_entry.get_date()
            fecha_final = fecha_final_entry.get_date()
            centro_acopio_seleccionado = centro_acopio_combobox.get()

            # Verificar si las fechas o el centro de acopio están vacíos
            if not fecha_inicio or not fecha_final or not centro_acopio_seleccionado:
                raise ValueError("Las fechas de inicio y fin, y el centro de acopio son obligatorios.")
        except ValueError as e:
            # Manejar errores de conversión de fecha, entrada inválida, fechas vacías o centro de acopio vacío
            messagebox.showerror("Error", f"Error al obtener las fechas o el centro de acopio: {e}")
            return

            #Verifica que la fecha final sea mayor a la inicial
        if fecha_inicio > fecha_final:
            messagebox.showerror("Error", "La fehca inicial no puede ser mayor a la fehca final.")
            return
        # Limpiar tabla de transacciones
        for item in transacciones_tree.get_children():
            transacciones_tree.delete(item)

        # Filtrar transacciones por fecha y centro de acopio
        filtered_transactions = []
        for transaccion in datos:
            try:
                trans_fecha = datetime.datetime.strptime(transaccion[0], "%m/%d/%Y").date()
            except ValueError as e:
                # Manejar errores en el formato de fecha de la transacción
                print(f"Error al convertir fecha de la transacción: {e}")
                continue
            trans_centro_acopio = transaccion[2]
            if fecha_inicio <= trans_fecha <= fecha_final and trans_centro_acopio == centro_acopio_seleccionado:
                filtered_transactions.append(transaccion)

        # Verificar si no se encontraron transacciones
        if not filtered_transactions:
            messagebox.showinfo("Información", "No se encontraron transacciones para los criterios seleccionados.")
        else:
            for transaccion in filtered_transactions:
                transacciones_tree.insert("", tk.END, values=transaccion)

    transaccion_frame.protocol("WM_DELETE_WINDOW", close_window)