from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")

lista = driver.find_element_by_xpath("""//*[@id="main"]/div[3]/div[1]/select""")
opciones = driver.find_elements_by_tag_name("option")

for opcion in opciones:
    sleep(1)
    opcion.click()

driver.quit()