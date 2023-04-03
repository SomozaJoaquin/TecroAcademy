import unittest
import cambia_texto
'''
Test que verifica si retorna lo que la funcion pide, en este caso, toda la frase debe ser devuelta en mayuscula.
'''
class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "BUEN DIA")

if __name__ == '__main__':
    unittest.main()
