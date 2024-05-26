import tkinter as tk
from tkinter import messagebox

from pantallas import sedes_pantalla, centrosacopio_panatlla, catalogo_materiales_pantalla, crear_transaccion_pntlla , historial_transacciones

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
    
    crear_button_transaccion = tk.Button(root, text="Crear transacción", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda: crear_transaccion_pntlla(root))
    crear_button_transaccion.place(x=250,y=200)
    
    crear_button_historial_ca = tk.Button(root, text="Historial de transacciones", font=("Bahnschrift Condensed", 14), fg="black", bg="#A5C0DD", borderwidth=4, command=lambda: historial_transacciones(root))
    crear_button_historial_ca.place(x=250,y=250)
    
    

    root.mainloop()
