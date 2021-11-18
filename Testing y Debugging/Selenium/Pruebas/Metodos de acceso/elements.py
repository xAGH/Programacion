from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")

varios = driver.find_elements_by_class_name("inputtext")
boton = driver.find_element_by_name("login")

for elemento in varios:
    elemento.send_keys("ARGUMENTOS")

boton.click()
driver.quit()