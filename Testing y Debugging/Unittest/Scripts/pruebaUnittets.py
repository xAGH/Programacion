from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest as uni

class menuDesplegable(uni.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Selenium\Pruebas\Drivers\chromedriver.exe")

    def test_recorrer(self):

        self.driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")

        # Se obtiene ele select con su respectivo xpath
        self.lista = Select(self.driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))

        # Para seleccionar un option por posicion:
        
        self.lista.select_by_index(6)

        # Para seleccionar un option por su value:
        
        self.lista.select_by_value("5")

        # Para seleccionar un option de acuierdo al texto visible:
        
        self.lista.select_by_visible_text("Nissan")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    uni.main()