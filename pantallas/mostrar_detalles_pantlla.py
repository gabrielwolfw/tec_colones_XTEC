import tkinter as tk


def mostrar_detalles(fecha, carnet_estudiante, sede, centro_acopio, cantidad_material, tec_colones, tipo,transaccion_frame):
    # Función para mostrar la ventana emergente con los detalles de la transacción
    detalles_frame = tk.Toplevel(transaccion_frame)
    detalles_frame.title("Detalles de la transacción")
    detalles_frame.geometry("400x300")

    # Labels con los detalles
    fecha_label = tk.Label(detalles_frame, text=f"Fecha: {fecha}", font=("Bahnschrift Condensed", 12))
    fecha_label.place(x=20, y=20)
    carnet_label = tk.Label(detalles_frame, text=f"Carnet del estudiante: {carnet_estudiante}", font=("Bahnschrift Condensed", 12))
    carnet_label.place(x=20, y=50)
    sede_label = tk.Label(detalles_frame, text=f"Sede: {sede}", font=("Bahnschrift Condensed", 12))
    sede_label.place(x=20, y=80)
    centro_label = tk.Label(detalles_frame, text=f"Centro de acopio: {centro_acopio}", font=("Bahnschrift Condensed", 12))
    centro_label.place(x=20, y=110)
    cantidad_label = tk.Label(detalles_frame, text=f"Cantidad: {cantidad_material}", font=("Bahnschrift Condensed", 12))
    cantidad_label.place(x=20, y=140)
    tec_colones_label = tk.Label(detalles_frame, text=f"TecColones: {tec_colones}", font=("Bahnschrift Condensed", 12))
    tec_colones_label.place(x=20, y=170)
    tipo_label = tk.Label(detalles_frame, text=f"Tipo: {tipo}", font=("Bahnschrift Condensed", 12))
    tipo_label.place(x=20, y=200)
