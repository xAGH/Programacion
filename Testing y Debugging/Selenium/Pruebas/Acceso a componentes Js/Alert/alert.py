from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get(r"file:///F:/Programacion/Testing%20y%20Debugging/Pruebas%20Testing/Pruebas/Acceso%20a%20componentes%20Js/Alert/html/alert.html")

boton = driver.find_element_by_id("btn")
sleep(3)
boton.click()

alert = driver.switch_to_alert()
sleep(3)
alert.dismiss()

driver.quit()