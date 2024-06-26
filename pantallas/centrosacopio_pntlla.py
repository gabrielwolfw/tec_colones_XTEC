import tkinter as tk
from tkinter import ttk

import pantallas_logica.centrosacopio_logica_pntlla as centrosacopio_logica_pntlla

def centrosacopio_panatlla(root):
    # Ocultar la ventana principal
    root.withdraw()

    centrosacopio_frame = tk.Toplevel(root)
    centrosacopio_frame.title("Administración de Sedes")
    centrosacopio_frame.geometry("400x300")
    centrosacopio_frame.resizable(False, False)
    centrosacopio_frame.configure(bg="#F1F6F9")

    nombresede_Label = tk.Label(centrosacopio_frame, text="Nombre de la sede:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    nombresede_Label.place(x=20, y=20)
    valores_sedes = centrosacopio_logica_pntlla.obtener_sedes_combobox()
    nombresede_Entry = tk.ttk.Combobox(centrosacopio_frame,values=valores_sedes,width=25)
    nombresede_Entry.place(x=200, y=20)

    numerocontacto_Label = tk.Label(centrosacopio_frame, text="Número de contacto:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    numerocontacto_Label.place(x=20, y=70)
    numerocontacto_Entry = tk.Entry(centrosacopio_frame, width=30)
    numerocontacto_Entry.place(x=200, y=70)

    identificador_Label = tk.Label(centrosacopio_frame, text="Identificador:", font=("Bahnschrift Condensed", 14), bg="#A5C0DD")
    identificador_Label.place(x=20, y=120)
    identificador_Entry = tk.Entry(centrosacopio_frame, width=30)
    identificador_Entry.place(x=200, y=120)

    crear_centro_acopio_button = tk.Button(centrosacopio_frame, text="Crear Centro de Acopio", command=lambda: centrosacopio_logica_pntlla.crear_centro_acopio(nombresede_Entry,
                                                                                                                                                                   numerocontacto_Entry,
                                                                                                                                                                   identificador_Entry), font=("Bahnschrift Condensed", 14))
    crear_centro_acopio_button.place(x=100, y=170)
    
    # Botón de Salir
    salir_button = tk.Button(centrosacopio_frame, text="Salir",font=("Bahnschrift Condensed", 12), bg="#A5C0DD", command=lambda: close_window())
    salir_button.place(x=350, y=260)

    def close_window():
        # Mostrar nuevamente la ventana principal
        root.deiconify()
        centrosacopio_frame.destroy()

    centrosacopio_frame.protocol("WM_DELETE_WINDOW", close_window)

