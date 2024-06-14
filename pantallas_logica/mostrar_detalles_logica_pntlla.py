from tkinter import messagebox
from gestion_transacciones import Transacciones
from manejador_archivos import guardar_transacciones_estado,verificar_transaccion_anulada


transaccion = Transacciones()


def anular_transaccion(fecha, carnet_estudiante, sede, centro_acopio, cantidad_material, tec_colones, tipo, identificador_t):
    if tipo == "Aprobada":
        if verificar_transaccion_anulada(identificador_t):
            messagebox.showwarning("Advertencia", "La transacción ya ha sido anulada anteriormente.")
        else:
            tec_colones = float(tec_colones)
            tec_colones = -tec_colones
            tec_colones = str(tec_colones)
            transaccion.anular_transaccion(carnet_estudiante, sede, centro_acopio, cantidad_material, tec_colones)
            guardar_transacciones_estado(identificador_t)
            messagebox.showinfo("Información", "Transacción anulada con éxito.")
    else:
        messagebox.showwarning("Advertencia", "No se puede anular una transacción que ya ha sido anulada.")

