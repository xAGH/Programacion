from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")

# Email con ruta xpath absouluta
# email = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]")

# Email con ruta xpath relativa
email = driver.find_element_by_xpath("//input[@data-testid='royal_email']")
clave = driver.find_element_by_xpath("//input[@aria-label='Contraseña']")
enviar = driver.find_element_by_xpath("//button[@data-testid='royal_login_button']")

email.send_keys("correo")
clave.send_keys("clave")
enviar.click()