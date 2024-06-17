from tkinter import messagebox
from gestion_transacciones import Transacciones
from manejador_archivos import guardar_transacciones_estado,verificar_transaccion_anulada, validar_existencia_archivo_transacciones_estado  


transaccion = Transacciones()


def anular_transaccion(fecha, carnet_estudiante, sede, centro_acopio, cantidad_material, tec_colones, tipo, identificador_t):
    if not validar_existencia_archivo_transacciones_estado():
        messagebox.showerror("Error", "El archivo transacciones_estado.txt no existe, contacte al administrador.")
        return
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

