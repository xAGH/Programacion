import unittest as uni
from selenium import webdriver

class espera_implicita(uni.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Selenium\Pruebas\Drivers\chromedriver.exe")
        self.driver.get("https://www.udemy.com/join/login-popup/?next=/home/my-courses/learning/")

    def test_usando_implicit_wait(self):
        # Se hace una espera de hasta maximo 5 segundos hasta que se cargue por completo la pagina.
        self.driver.implicitly_wait(5)
        self.usuario = self.driver.find_element_by_name("email")
        self.usuario.send_keys("alejopruebas23021@gmail.com")

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    uni.main()