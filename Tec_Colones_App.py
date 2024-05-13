import tkinter as tk
from tkinter import messagebox

from pantallas import sedes_pantalla, centrosacopio_panatlla, catalogo_materiales_pantalla

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    root.title("TecColones App")
    root.geometry("600x400")
    root.configure(bg="#F1F6F9")

    crear_button_catalogomateriales = tk.Button(root, text="Crear material", font=("Bahnschrift Condensed", 14), fg="black",bg="#A5C0DD", borderwidth=4, command=lambda: catalogo_materiales_pantalla(root))
    crear_button_catalogomateriales.place(x=250,y=50)

    crear_button_sede = tk.Button(root, text="Crear sede", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda: sedes_pantalla(root))
    crear_button_sede.place(x=250,y=100)

    crear_button_centroacopio = tk.Button(root, text="Crear centro de acopio", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda: centrosacopio_panatlla(root))
    crear_button_centroacopio.place(x=250,y=150)

    root.mainloop()
