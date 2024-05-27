import tkinter as tk
from tkinter import ttk
import datetime
import tkcalendar
transacción_seleccionada= None

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
    fecha_inicio_entry = DateEntry(transaccion_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    fecha_inicio_entry.place(x=120, y=20)

    fecha_final_label = tk.Label(transaccion_frame, text="Fecha final", font=("Bahnschrift Condensed", 12))
    fecha_final_label.place(x=250, y=20)
    fecha_final_entry = DateEntry(transaccion_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    fecha_final_entry.place(x=340, y=20)

    centro_acopio_label = tk.Label(transaccion_frame, text="Centro de acopio", font=("Bahnschrift Condensed", 12))
    centro_acopio_label.place(x=470, y=20)
    centro_acopio_combobox = ttk.Combobox(transaccion_frame, values=["CMF1", "CMFP"], font=("Bahnschrift Condensed", 12))
    centro_acopio_combobox.place(x=570, y=20)
    centro_acopio_combobox.current(0)

    buscar_button = tk.Button(transaccion_frame, text="Buscar", font=("Bahnschrift Condensed", 12), bg="#A5C0DD", command= lambda: buscar_transacciones())
    buscar_button.place(x=745, y=15)

    # Tabla de transacciones
    columnas = ("Fecha", "Carnet estudiante", "Cantidad material", "Centro de acopio", "TecColones", "Tipo")
    transacciones_tree = ttk.Treeview(transaccion_frame, columns=columnas, show="headings")
    transacciones_tree.place(x=20, y=60, width=760, height=280)

    for col in columnas:
        transacciones_tree.heading(col, text=col)
        transacciones_tree.column(col, width=100)

    # Datos de ejemplo
    datos = [
        ("12/10/2024", "102030330", "12", "CMF1", "-500", "Anulada"),
        ("12/03/2024", "102030330", "34", "CMF1", "-500", "Anulada"),
        ("12/23/2024", "102030330", "12", "CMF1", "457", "Anulada"),
        ("05/09/2024", "155050350", "1", "CMFP", "10", "Aprobada"),
        ("12/10/2024", "102030330", "12", "CMFP", "-500", "Anulada"),
        ("12/03/2024", "102030330", "34", "CMFP", "-500", "Anulada"),
        ("12/23/2024", "102030330", "12", "CMFP", "457", "Anulada"),
        ("05/09/2024", "155050350", "1", "CMFP", "10", "Aprobada"),
        ("09/02/2024", "199931200", "22", "CMF1", "1000", "Aprobada")
    ]

    for item in datos:
        transacciones_tree.insert("", tk.END, values=item)

    # Botón de Ver Detalles
    ver_detalles_button = tk.Button(transaccion_frame, text="Ver detalles", font=("Bahnschrift Condensed", 12), bg="#A5C0DD", command= lambda: mostrar_detalles())
    ver_detalles_button.place(x=695, y=350)

    # Botón de Salir
    salir_button = tk.Button(transaccion_frame, text="Salir", font=("Bahnschrift Condensed", 12), bg="#A5C0DD", command=lambda: close_window())
    salir_button.place(x=20, y=350)

    def close_window():
        # Mostrar nuevamente la ventana principal
        root.deiconify()
        transaccion_frame.destroy()
        
    def mostrar_detalles():
        # Obtener la transacción seleccionada
        global transaccion_seleccionada
        transaccion_seleccionada = transacciones_tree.focus()
        if transaccion_seleccionada:
            valores = transacciones_tree.item(transaccion_seleccionada)['values']
            fecha, carnet_estudiante, cantidad_material, centro_acopio, tec_colones, tipo = valores

            # Función para mostrar la ventana emergente con los detalles de la transacción
            detalles_frame = tk.Toplevel(transaccion_frame)
            detalles_frame.title("Detalles de la transacción")
            detalles_frame.geometry("400x300")

            # Labels con los detalles
            fecha_label = tk.Label(detalles_frame, text=f"Fecha: {fecha}", font=("Bahnschrift Condensed", 12))
            fecha_label.place(x=20, y=20)
            carnet_label = tk.Label(detalles_frame, text=f"Carnet del estudiante: {carnet_estudiante}", font=("Bahnschrift Condensed", 12))
            carnet_label.place(x=20, y=50)
            cantidad_label = tk.Label(detalles_frame, text=f"Cantidad de material: {cantidad_material}", font=("Bahnschrift Condensed", 12))
            cantidad_label.place(x=20, y=80)
            centro_label = tk.Label(detalles_frame, text=f"Centro de acopio: {centro_acopio}", font=("Bahnschrift Condensed", 12))
            centro_label.place(x=20, y=110)
            tec_colones_label = tk.Label(detalles_frame, text=f"TecColones: {tec_colones}", font=("Bahnschrift Condensed", 12))
            tec_colones_label.place(x=20, y=140)
            tipo_label = tk.Label(detalles_frame, text=f"Tipo: {tipo}", font=("Bahnschrift Condensed", 12))
            tipo_label.place(x=20, y=170)
            
    def buscar_transacciones():
        fecha_inicio = fecha_inicio_entry.get_date()
        fecha_final = fecha_final_entry.get_date()
        centro_acopio_seleccionado = centro_acopio_combobox.get()

        # Limpiar tabla de transacciones
        for item in transacciones_tree.get_children():
            transacciones_tree.delete(item)

        # Filtrar transacciones por fecha y centro de acopio
        for transaccion in datos:
            trans_fecha = datetime.datetime.strptime(transaccion[0], "%m/%d/%Y").date()
            trans_centro_acopio = transaccion[3]
            if fecha_inicio <= trans_fecha <= fecha_final and trans_centro_acopio == centro_acopio_seleccionado:
                transacciones_tree.insert("", tk.END, values=transaccion)
            
            
    transaccion_frame.protocol("WM_DELETE_WINDOW", close_window)