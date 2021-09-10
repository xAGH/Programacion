from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F&persist_locale=")

# Selenium no reconoce la ñ
has_olvidado_contrasena = driver.find_element_by_link_text("Forgot Password")
has_olvidado_contrasena.click()

driver.quit()