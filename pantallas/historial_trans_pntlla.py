import tkinter as tk
from tkinter import ttk
import datetime
from tkcalendar import DateEntry
import pantallas_logica.crear_transacciones_logica_pntlla as transaccion_logica
from pantallas_logica.historial_trans_logica_pantlla import ingresa_datos_transacciones,buscar_transacciones,abrir_mostrar_detalles,close_window
from manejador_archivos.transacciones_manejador_archivos import leer_datos_de_transacciones


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

    valores_centros_acopio = transaccion_logica.obtener_centros_acopio_combobox()
    centro_acopio_label = tk.Label(transaccion_frame, text="Centro de acopio", font=("Bahnschrift Condensed", 12))
    centro_acopio_label.place(x=470, y=20)
    centro_acopio_combobox = ttk.Combobox(transaccion_frame,values=valores_centros_acopio, font=("Bahnschrift Condensed", 12))
    centro_acopio_combobox.place(x=570, y=20)
    centro_acopio_combobox.current(0)

    datos = leer_datos_de_transacciones()

    buscar_button = tk.Button(transaccion_frame, text="Buscar", font=("Bahnschrift Condensed", 12), bg="#A5C0DD", command= lambda: buscar_transacciones(transacciones_tree,fecha_inicio_entry,fecha_final_entry,centro_acopio_combobox,datos))
    buscar_button.place(x=745, y=15)

    # Tabla de transacciones
    columnas = ("Fecha", "Carnet estudiante", "Centro de acopio", "Material:Cantidad", "TecColones", "Tipo")
    transacciones_tree = ttk.Treeview(transaccion_frame, columns=columnas, show="headings")
    transacciones_tree.place(x=20, y=60, width=760, height=280)



    ingresa_datos_transacciones(transacciones_tree,columnas,datos)
    

    # Botón de Ver Detalles
    ver_detalles_button = tk.Button(transaccion_frame, text="Ver detalles", font=("Bahnschrift Condensed", 12), bg="#A5C0DD", command= lambda: abrir_mostrar_detalles(transacciones_tree,transaccion_frame))
    ver_detalles_button.place(x=695, y=350)

    # Botón de Salir
    salir_button = tk.Button(transaccion_frame, text="Salir", font=("Bahnschrift Condensed", 12), bg="#A5C0DD", command=lambda: close_window(root, transaccion_frame))
    salir_button.place(x=20, y=350)


            
    transaccion_frame.protocol("WM_DELETE_WINDOW", lambda: close_window(root, transaccion_frame))