import unittest as uni

class metodosUnittest(uni.TestCase):

    # Metodo de inicializacion a nivel de clase.
    @classmethod
    def setUpClass(cls):
        print("Este metodo inicia cuando empieza la clase")

    # Predefinir condiciones antes de realizar cada test case 
    def setUp(self):
        print("Yo me inicio en cada test case")

    # Creacion de test, por ello se inicia con test_...
    def test_mensaje(self):
        print("Yo soy el test case del mensaje")

    # Creacion de test, por ello se inicia con test_...
    def testNumero(self):
        print("Yo soy el test case del numero")

    # Finalizacion de cada test case
    def tearDown(self):
        print("Yo finalizo la ejecucion de cada test case")

    # Metodo de finalizacion a nivel de clase
    @classmethod
    def tearDownClass(cls):
        print("Este metodo se ejecuta al final de la clase")

if __name__ == '__main__':
    uni.main()