from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get(r"file:///F:/Programacion/Testing%20y%20Debugging/Pruebas%20Testing/Pruebas/Acceso%20a%20componentes%20Js/Confirm/html/confirm.html")

boton = driver.find_element_by_name("boton")
sleep(3)
boton.click()

confirm = driver.switch_to_alert()

# Con esto cancela la alerta
# sleep(3)
#confirm.dismiss()

# Con esto se acepta la alerta
sleep(3)
confirm.accept()

driver.quit