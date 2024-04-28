class Lista_materiales:
    def __init__(self):
        self.materiales = []

    def agregar_material(self, material):
        self.materiales.append(material)
        self.mostrar_materiales()

    def mostrar_materiales(self):
        print("Lista de materiales:")
        for i, material in enumerate(self.materiales, start=1):
            print((i), ".", (material))
        print()
lista = Lista_materiales()
