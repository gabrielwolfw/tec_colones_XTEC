import unittest
import CatalogoMateriales
from tkinter import messagebox

class TestCatalogoMateriales(unittest.TestCase):
    def setUp(self):
        self.catalogo = CatalogoMateriales.CatalogoMaterialesReciclaje()

    def test_crear_material_reciclaje(self):
        # Caso material de reciclaje creado
        self.assertTrue(self.catalogo.crear_material_reciclaje("Papel", "kilogramo", 500, "Material reciclable"))
    
        # Caso material de reciclaje con nombre menor a 5 caracteres
        with self.assertRaises(ValueError):
            self.catalogo.crear_material_reciclaje("Pap", "kilogramo", 500, "Material reciclable")
            
        # Caso material de reciclaje con nombre mayor a 50 caracteres
        with self.assertRaises(ValueError):
            self.catalogo.crear_material_reciclaje("Papel"*11, "kilogramo", 500, "Material reciclable")
            
        # Caso material de reciclaje con unidad no válida
        with self.assertRaises(ValueError):
            self.catalogo.crear_material_reciclaje("Papel", "gramo", 500, "Material reciclable")
            
        # Caso material de reciclaje con valor unitario menor a 0
        with self.assertRaises(ValueError):
            self.catalogo.crear_material_reciclaje("Papel", "gramo", -1, "Material reciclable")

    def test_generar_identificador_unico(self):
        # Prueba de generación de identificador único
        identificador1 = self.catalogo.generar_identificador_unico()
        identificador2 = self.catalogo.generar_identificador_unico()
        self.assertNotEqual(identificador1, identificador2)

if __name__ == "__main__":
    unittest.main()