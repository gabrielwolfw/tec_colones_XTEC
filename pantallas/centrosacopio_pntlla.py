import tkinter as tk

import pantallas.logica_centrosacopio_pntlla as logica_centrosacopio_pntlla

def centrosacopio_panatlla(root):
    centrosacopio_frame = tk.Toplevel(root)
    centrosacopio_frame.title("Administración de Sedes")
    centrosacopio_frame.geometry("400x300")
    centrosacopio_frame.resizable(False, False)

    nombresede_Label = tk.Label(centrosacopio_frame, text="Nombre de la sede:")
    nombresede_Label.pack()
    nombresede_Entry = tk.Entry(centrosacopio_frame, width=30)
    nombresede_Entry.pack()

    numerocontacto_Label = tk.Label(centrosacopio_frame, text="Número de contacto:")
    numerocontacto_Label.pack()
    numerocontacto_Entry = tk.Entry(centrosacopio_frame, width=30)
    numerocontacto_Entry.pack()

    identificador_Label = tk.Label(centrosacopio_frame, text="Identificador:")
    identificador_Label.pack()
    identificador_Entry = tk.Entry(centrosacopio_frame, width=30)
    identificador_Entry.pack()

    crear_centro_acopio_button = tk.Button(centrosacopio_frame, text="Crear Centro de Acopio", 
                                           command=lambda: logica_centrosacopio_pntlla.crear_centro_acopio(nombresede_Entry.get(),
                                                                                numerocontacto_Entry.get(),
                                                                                identificador_Entry.get()))
    crear_centro_acopio_button.pack()





