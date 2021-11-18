from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.udemy.com/")

# Abrir nueva pestaña
driver.execute_script("window.open('');")

# Moverse entre pestañas 
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

# Eliminar primera pestaña
driver.switch_to.window(driver.window_handles[0])
driver.close()

driver.quit()