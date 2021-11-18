from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

email = driver.find_element_by_class_name("form-control")
clave = driver.find_element_by_class_name("textinput")
enviar = driver.find_element_by_class_name("btn")

email.send_keys("alejopruebas23001@gmail.com")
clave.send_keys("alejo12345")
enviar.click()

driver.quit()