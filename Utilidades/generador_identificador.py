import secrets
import hashlib

identificadores_existentes = set()
'''
Método para generar un identificador único para un material
 '''
def generar_identificador_unico():
    while True:
        token = secrets.token_hex(6)
        hash_object = hashlib.sha256(token.encode())
        hash_token = hash_object.hexdigest()[:12]
        key_id = hash_token
        if key_id not in identificadores_existentes:
            return key_id