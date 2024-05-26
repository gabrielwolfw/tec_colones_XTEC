import tkinter as tk
from tkinter import ttk

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

    centro_Label = tk.Label(transaccion_frame, text="Seleccione el centro de acopio:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    centro_Label.place(x=20, y=70)
    centro_combobox = tk.ttk.Combobox(transaccion_frame, values=["", "", ""], font=("Bahnschrift Condensed", 14))
    centro_combobox.place(x=228, y=72)
    centro_combobox.current(0)
    
    material_Label = tk.Label(transaccion_frame, text="Seleccione el tipo de material:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    material_Label.place(x=20, y=117)
    material_combobox = tk.ttk.Combobox(transaccion_frame, values=[",", ",", ","], font=("Bahnschrift Condensed", 14))
    material_combobox.place(x=228, y=119)
    material_combobox.current(0)
    
    cantidad_Label = tk.Label(transaccion_frame, text="Ingrese la cantidad de material:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    cantidad_Label.place(x=20, y=164)
    cantidad_Entry = tk.Entry(transaccion_frame, width=30)
    cantidad_Entry.place(x=237, y=169)
    
    
    agregar_button = tk.Button(transaccion_frame, text="Agregar", bg="#A5C0DD")
    agregar_button.place(x=365, y=210)
    
    columna = ("Material", "Valor")
    materiales_ag = ttk.Treeview(transaccion_frame, columns=columna, show="headings", height=5)
    materiales_ag.place(x=20, y=250)
    materiales_ag.heading("Material", text="Material")
    materiales_ag.heading("Valor", text="Valor")
    materiales_ag.column("Material", width=70)
    materiales_ag.column("Valor", width=70)
    
    datos = [
        ("Material 1", "valor 1"),
        ("Material 2", "valor 2"),
        ("Material 3", "valor 3"),
        ("Material 4", "valor 4"),
        ("Material 5", "valor 5"),
        ("Material 6", "valor 6"),
        ("Material 7", "valor 7")
    ]
    
    for item in datos:
        materiales_ag.insert("", tk.END, values=item)
        
    colones_Label = tk.Label(transaccion_frame, text="Cantidad de Tec-Colones para asignar:", font=("Bahnschrift Condensed", 14))
    colones_Label.place(x=20, y=400)
    
    salir_button = tk.Button(transaccion_frame, text="Salir", bg="#A5C0DD", font=("Bahnschrift Condensed", 12), command=lambda:close_window())
    salir_button.place(x=12, y=460)
    
    continuar_button = tk.Button(transaccion_frame, text="Continuar", bg="#A5C0DD",font=("Bahnschrift Condensed", 12))
    continuar_button.place(x=530, y=460)
    


    def close_window():
        # Mostrar nuevamente la ventana principal
        root.deiconify()
        transaccion_frame.destroy()

    transaccion_frame.protocol("WM_DELETE_WINDOW", close_window)

