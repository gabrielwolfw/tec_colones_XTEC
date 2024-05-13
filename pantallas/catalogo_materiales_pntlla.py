import tkinter as tk
from tkinter import ttk
from pantallas.logica_catalogo_materiales_pntlla import crear_material,actualizar_lista


def catalogo_materiales_pantalla(root):
    # Ocultar la ventana principal
    root.withdraw()

    catalogo_frame = tk.Toplevel(root)
    catalogo_frame.title("Crear material de reciclaje")
    catalogo_frame.geometry("815x430")
    catalogo_frame.resizable(True, True)
    catalogo_frame.configure(bg="#F1F6F9")

    def close_window():
        # Mostrar nuevamente la ventana principal
        root.deiconify()
        catalogo_frame.destroy()

    catalogo_frame.protocol("WM_DELETE_WINDOW", close_window)

    nombre_label = tk.Label(catalogo_frame, text="Nombre del material:", font=("Bahnschrift Condensed", 14),bg="#A5C0DD")
    nombre_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    nombre_entry = tk.Entry(catalogo_frame)
    nombre_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    unidad_label = tk.Label(catalogo_frame, text="Unidad:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    unidad_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    unidad_combobox = tk.ttk.Combobox(catalogo_frame, values=["kilogramo", "litro", "unidad"], font=("Bahnschrift Condensed", 14))
    unidad_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    unidad_combobox.current(0)

    valor_label = tk.Label(catalogo_frame, text="Valor Unitario:", font=("Bahnschrift Condensed", 14),bg="#A5C0DD")
    valor_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    valor_entry = tk.Entry(catalogo_frame)
    valor_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    descripcion_label = tk.Label(catalogo_frame, text="Descripción:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    descripcion_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    descripcion_text = tk.Text(catalogo_frame, height=4, width=30)
    descripcion_text.grid(row=3, column=1, padx=5, pady=5, sticky="w")


    

    lista_label = tk.Label(catalogo_frame, text="Lista de materiales:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    lista_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    lista_text = tk.Text(catalogo_frame, height=10, width=100)
    lista_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


    crear_button = tk.Button(catalogo_frame, text="Crear", command=lambda: crear_material(nombre_entry,
                                                                                          unidad_combobox,
                                                                                          valor_entry,
                                                                                          descripcion_text,
                                                                                          lista_text), font=("Bahnschrift Condensed", 14))
    crear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    actualizar_lista(lista_text)

    




