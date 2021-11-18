from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get(r"file:///F:/Programacion/Testing%20y%20Debugging/Pruebas%20Testing/Pruebas/Acceso%20a%20componentes%20Js/Promt/html/promt.html")

boton = driver.find_element_by_id("btn")
sleep(3)
boton.click()

promt = driver.switch_to_alert()

# Con esto cancela la alerta
# sleep(3)
#promt.dismiss()

# Con esto se acepta la alerta
sleep(3)

# Se envia el valor a poner el en promt
promt.send_keys("Alejo")
promt.accept()

driver.quit