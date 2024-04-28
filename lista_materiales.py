import secrets
import hashlib

class Lista_materiales:
    def __init__(self):
        self.materiales = []
        self.identificadores_existentes = set()

    def agregar_material(self, material):
        material['identificador'] = self.generaunico_identificador(self.identificadores_existentes)
        self.materiales.append(material)
        self.mostrar_materiales()
        self.identificadores_existentes(material['identificador'])

    def mostrar_materiales(self):
        print("Lista de materiales:")
        for i, material in enumerate(self.materiales, start=1):
            print((i), ".", (material))
        print()

    def generaunico_identificador(self, existing_identifiers):
        while True:
            # Genera un token aleatorio de 12 caracteres alfanuméricos
            token = secrets.token_hex(6)  #token_hex genera 2 caracteres por byte
            # Crea un hash del token para asegurarse de que no sea consecutivo
            hash_object = hashlib.sha256(token.encode())
            hash_token = hash_object.hexdigest()[:12]
            # Crea la llave identificadora completa
            key_id = f"M-{hash_token}"
            # Verifica si el identificador es único
            if key_id not in existing_identifiers:
                return key_id
            # Si ya existe, intenta generar otro
lista = Lista_materiales()