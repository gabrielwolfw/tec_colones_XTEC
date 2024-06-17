import tkinter as tk
from tkinter import messagebox

from pantallas import autenticacion_pantalla

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    root.title("TecColones App")
    root.geometry("600x400")
    root.configure(bg="#F1F6F9")
    
    autenticacion_pantalla(root)

    root.mainloop()
