from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")

email = driver.find_element(By.ID,"email")
clave = driver.find_element(By.ID, "pass")
boton = driver.find_element(By.NAME, "login")

email.send_keys("correo")
clave.send_keys("clave")
boton.click()
driver.quit()