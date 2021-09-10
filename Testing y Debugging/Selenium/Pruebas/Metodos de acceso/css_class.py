from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")

email = driver.find_element_by_css_selector("input._6luy")
clave = driver.find_element_by_css_selector("input#pass")
boton = driver.find_element_by_name("login")

email.send_keys("correo")
clave.send_keys("clave")

boton.click()
driver.quit()