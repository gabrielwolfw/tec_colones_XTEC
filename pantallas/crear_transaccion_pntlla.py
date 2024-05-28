import tkinter as tk
from tkinter import ttk
import pantallas_logica.crear_transacciones_logica_pntlla as transaccion_logica

def crear_transaccion_pntlla(root):
    # Ocultar la ventana principal
    root.withdraw()

    transaccion_frame = tk.Toplevel(root)
    transaccion_frame.title("Crear transacción")
    transaccion_frame.geometry("600x500")
    transaccion_frame.resizable(False, False)
    transaccion_frame.configure(bg="#F1F6F9")

    carnet_Label = tk.Label(transaccion_frame, text="Ingrese el número de carnet:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    carnet_Label.place(x=20, y=20)
    carnet_Entry = tk.Entry(transaccion_frame, width=30)
    carnet_Entry.place(x=220, y=25)

    valores_centros_acopio = transaccion_logica.obtener_centros_acopio_combobox()
    centro_Label = tk.Label(transaccion_frame, text="Seleccione el centro de acopio:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    centro_Label.place(x=20, y=70)
    centro_combobox = tk.ttk.Combobox(transaccion_frame, values=valores_centros_acopio, font=("Bahnschrift Condensed", 14))
    centro_combobox.place(x=228, y=72)
    centro_combobox.current(0)
    
    material_Label = tk.Label(transaccion_frame, text="Seleccione el tipo de material:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    material_Label.place(x=20, y=117)
    valores_combobox = transaccion_logica.obtener_materiales_combobox()
    material_combobox = tk.ttk.Combobox(transaccion_frame, values=valores_combobox, font=("Bahnschrift Condensed", 14))
    material_combobox.place(x=228, y=119)
    material_combobox.current(0)
    
    cantidad_Label = tk.Label(transaccion_frame, text="Ingrese la cantidad de material:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    cantidad_Label.place(x=20, y=164)
    cantidad_Entry = tk.Entry(transaccion_frame, width=30)
    cantidad_Entry.place(x=237, y=169)
    
    
    
    
    columna = ("Material", "Valor")
    materiales_ag = ttk.Treeview(transaccion_frame, columns=columna, show="headings", height=5)
    materiales_ag.place(x=20, y=250)
    materiales_ag.heading("Material", text="Material")
    materiales_ag.heading("Valor", text="Valor")
    materiales_ag.column("Material", width=70)
    materiales_ag.column("Valor", width=70)
    
    datos = []
    for item in datos:
        materiales_ag.insert("", tk.END, values=item)
    



    colones_Label = tk.Label(transaccion_frame, text="Cantidad de Tec-Colones para asignar:", font=("Bahnschrift Condensed", 14))
    colones_Label.place(x=20, y=400)
    total_tec_colones_Entry = tk.Entry(transaccion_frame, width=30, state=tk.DISABLED)
    total_tec_colones_Entry.place(x=280, y=410)
    total_tec_colones_Entry.config(state=tk.NORMAL)
    total_tec_colones_Entry.insert(0, "0.00")
    total_tec_colones_Entry.config(state=tk.DISABLED)

    agregar_button = tk.Button(transaccion_frame, text="Agregar", bg="#A5C0DD",command=lambda:transaccion_logica.agregar_material_transaccion(material_combobox,cantidad_Entry,materiales_ag,total_tec_colones_Entry))
    agregar_button.place(x=365, y=210)
    
    salir_button = tk.Button(transaccion_frame, text="Salir", bg="#A5C0DD", font=("Bahnschrift Condensed", 12), command=lambda:transaccion_logica.close_window(root,transaccion_frame))
    salir_button.place(x=12, y=460)
    
    continuar_button = tk.Button(transaccion_frame, text="Continuar", bg="#A5C0DD",font=("Bahnschrift Condensed", 12), command=lambda:transaccion_logica.continuar_click(carnet_Entry, centro_combobox, total_tec_colones_Entry, cantidad_Entry, materiales_ag))
    continuar_button.place(x=530, y=460)



    transaccion_frame.protocol("WM_DELETE_WINDOW", lambda:transaccion_logica.close_window(root,transaccion_frame))

