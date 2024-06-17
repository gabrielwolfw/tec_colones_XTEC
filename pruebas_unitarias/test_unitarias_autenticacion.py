# pruebas_unitarias/test_pruebas_unitarias_auth.py
import unittest
from unittest.mock import MagicMock, patch

class TestAutenticacion(unittest.TestCase):

    @patch('pantallas_logica.auten_logica_pntlla.messagebox.showerror')
    @patch('pantallas.pantalla_menu.mostrar_pantalla_admin')
    @patch('pantallas.pantalla_menu.mostrar_pantalla_encargado')
    @patch('pantallas.pantalla_menu.mostrar_pantalla_estudiante')
    def test_iniciar_sesion_admin(self, mock_estudiante, mock_encargado, mock_admin, mock_showerror):
        from pantallas_logica.auten_logica_pntlla import iniciar_sesion
        correo_entry = MagicMock()
        contrasena_entry = MagicMock()
        auth_frame = MagicMock()
        root = MagicMock()

        correo_entry.get.return_value = "admin@tec.ac.cr"
        contrasena_entry.get.return_value = "1234abcd"
        
        iniciar_sesion(correo_entry, contrasena_entry, auth_frame, root)
        
        auth_frame.destroy.assert_called_once()
        mock_admin.assert_called_once_with(root)
        mock_encargado.assert_not_called()
        mock_estudiante.assert_not_called()
        mock_showerror.assert_not_called()

    @patch('pantallas_logica.auten_logica_pntlla.messagebox.showerror')
    @patch('pantallas.pantalla_menu.mostrar_pantalla_admin')
    @patch('pantallas.pantalla_menu.mostrar_pantalla_encargado')
    @patch('pantallas.pantalla_menu.mostrar_pantalla_estudiante')
    def test_iniciar_sesion_encargado(self, mock_estudiante, mock_encargado, mock_admin, mock_showerror):
        from pantallas_logica.auten_logica_pntlla import iniciar_sesion
        correo_entry = MagicMock()
        contrasena_entry = MagicMock()
        auth_frame = MagicMock()
        root = MagicMock()

        correo_entry.get.return_value = "centro@tec.ac.cr"
        contrasena_entry.get.return_value = "9900abcd"
        
        iniciar_sesion(correo_entry, contrasena_entry, auth_frame, root)
        
        auth_frame.destroy.assert_called_once()
        mock_admin.assert_not_called()
        mock_encargado.assert_called_once_with(root)
        mock_estudiante.assert_not_called()
        mock_showerror.assert_not_called()

    @patch('pantallas_logica.auten_logica_pntlla.messagebox.showerror')
    @patch('pantallas.pantalla_menu.mostrar_pantalla_admin')
    @patch('pantallas.pantalla_menu.mostrar_pantalla_encargado')
    @patch('pantallas.pantalla_menu.mostrar_pantalla_estudiante')
    def test_iniciar_sesion_estudiante(self, mock_estudiante, mock_encargado, mock_admin, mock_showerror):
        from pantallas_logica.auten_logica_pntlla import iniciar_sesion
        correo_entry = MagicMock()
        contrasena_entry = MagicMock()
        auth_frame = MagicMock()
        root = MagicMock()

        correo_entry.get.return_value = "estudiante@tec.ac.cr"
        contrasena_entry.get.return_value = "56789abcd"
        
        iniciar_sesion(correo_entry, contrasena_entry, auth_frame, root)
        
        auth_frame.destroy.assert_called_once()
        mock_admin.assert_not_called()
        mock_encargado.assert_not_called()
        mock_estudiante.assert_called_once_with(root)
        mock_showerror.assert_not_called()

    @patch('pantallas_logica.auten_logica_pntlla.messagebox.showerror')
    def test_iniciar_sesion_credenciales_vacias(self, mock_showerror):
        from pantallas_logica.auten_logica_pntlla import iniciar_sesion
        correo_entry = MagicMock()
        contrasena_entry = MagicMock()
        auth_frame = MagicMock()
        root = MagicMock()

        correo_entry.get.return_value = ""
        contrasena_entry.get.return_value = ""
        
        iniciar_sesion(correo_entry, contrasena_entry, auth_frame, root)
        
        auth_frame.destroy.assert_not_called()
        mock_showerror.assert_called_once_with("Error", "Por favor, ingrese sus credenciales")

    @patch('pantallas_logica.auten_logica_pntlla.messagebox.showerror')
    def test_iniciar_sesion_credenciales_incorrectas(self, mock_showerror):
        from pantallas_logica.auten_logica_pntlla import iniciar_sesion
        correo_entry = MagicMock()
        contrasena_entry = MagicMock()
        auth_frame = MagicMock()
        root = MagicMock()

        correo_entry.get.return_value = "wrong@tec.ac.cr"
        contrasena_entry.get.return_value = "wrongpass"
        
        iniciar_sesion(correo_entry, contrasena_entry, auth_frame, root)
        
        auth_frame.destroy.assert_not_called()
        mock_showerror.assert_called_once_with("Error", "Credenciales incorrectas")

    @patch('pantallas.autenticacion_pntlla.autenticacion_pantalla')
    def test_cerrar_sesion(self, mock_autenticacion_pantalla):
        from pantallas_logica.auten_logica_pntlla import cerrar_sesion
        root = MagicMock()
        cerrar_sesion(root)
        mock_autenticacion_pantalla.assert_called_once_with(root)

if __name__ == '__main__':
    unittest.main()
