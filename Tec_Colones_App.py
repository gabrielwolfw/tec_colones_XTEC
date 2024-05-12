import tkinter as tk
from tkinter import ttk, messagebox


from pantallas import sedes_pantalla, centrosacopio_panatlla,catalogo_materiales_pantalla

if __name__ == "__main__": 
    # Crear la ventana principal
    root = tk.Tk()
    root.title("TecColones App")
    root.geometry("600x400")

    crear_button_catalogomateriales = tk.Button(root, text="Crear material", command= lambda:catalogo_materiales_pantalla(root))
    crear_button_catalogomateriales.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    crear_button_sede = tk.Button(root, text="Crear sede", command=lambda: sedes_pantalla(root))
    crear_button_sede.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    crear_button_centroacopio = tk.Button(root, text="Crear centro de acopio", command=lambda:centrosacopio_panatlla(root))
    crear_button_centroacopio.grid(row=9, column=0, columnspan=2, padx=5, pady=5)


    root.mainloop()
