import requests

def validar_carnet(carnet):
    url = 'https://cuentatec.azurewebsites.net/api/StudentValidator'
    data = {"carnet": carnet}
    try:
        response = requests.get(url, json=data)
        response_data = response.json()
        
        if response.status_code == 200:
            return True, response.status_code, response_data.get("Mensaje", "Carnet válido")
        elif response.status_code == 400:
            return False, response.status_code, response_data.get("Solicitud incorrecta", "Falta la propiedad 'carnet' o entrada no válida")
        elif response.status_code == 404:
            return False, response.status_code, response_data.get("No válido", "No se encontró el recurso solicitado")
        elif response.status_code == 500:
            return False, response.status_code, response_data.get("Error interno del servidor", "Error interno del servidor")
    except Exception as e:
        return False, 0, str(e)