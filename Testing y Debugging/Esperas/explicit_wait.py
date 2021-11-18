import unittest as uni
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class espera_explicita(uni.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Selenium\Pruebas\Drivers\chromedriver.exe")
    
    def test_usando_explicit_wait(self):
        self.driver.get("https://www.udemy.com/join/login-popup/?next=/home/my-courses/learning/")
        try:
            # Espera explicita de 10 segundos que se hace hasta encontrar un elemento con el name de "email"
            element = wait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
            element.send_keys("alejopruebas2021@gmail.com")

        finally:
            self.driver.quit()

if __name__ == '__main__':
    uni.main()