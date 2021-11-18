from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")

# Se obtiene ele select con su respectivo xpath
lista = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))

# Para seleccionar un option por posicion:
sleep(3)
lista.select_by_index(6)

# Para seleccionar un option por su value:
sleep(3)
lista.select_by_value("5")

# Para seleccionar un option de acuierdo al texto visible:
sleep(3)
lista.select_by_visible_text("Nissan")



driver.quit()