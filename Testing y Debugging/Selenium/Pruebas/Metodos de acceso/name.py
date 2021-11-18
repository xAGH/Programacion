from selenium import webdriver as wb

driver = wb.Chrome(executable_path="F:\Programacion\Testing y Debugging\Selenium\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

email = driver.find_element_by_name("email")
clave = driver.find_element_by_name("password")
enviar = driver.find_element_by_name("submit")

email.send_keys("alejopruebas23001@gmail.com")
clave.send_keys("alejo12345")
enviar.click()

driver.quit()