import requests

def validar_carnet(carnet):
    url = 'https://cuentatec.azurewebsites.net/api/StudentValidator'
    data = {"carnet": carnet}
    print(data)
    try:
        response = requests.get(url, json=data)
        response_data = response.json()

        if response.status_code == 200:
            return True, response.status_code, response_data.get("Mensaje", "Carnet válido")
        elif response.status_code == 400:
            return False, response.status_code, response_data.get("Mensaje", "Solicitud incorrecta: Falta la propiedad 'carnet' o entrada no válida")
        elif response.status_code == 404:
            return False, response.status_code, response_data.get("Mensaje", "No válido: No se encontró el recurso solicitado")
        elif response.status_code == 500:
            return False, response.status_code, response_data.get("Mensaje", "Error interno del servidor")
        else:
            return False, response.status_code, response_data.get("Mensaje", "Error desconocido")
    except requests.exceptions.RequestException as e:
        return False, 0, f"Error de conexión: {str(e)}"
    except ValueError as e:
        return False, 0, f"Error al procesar la respuesta JSON: {str(e)}"
    except Exception as e:
        return False, 0, f"Error inesperado: {str(e)}"