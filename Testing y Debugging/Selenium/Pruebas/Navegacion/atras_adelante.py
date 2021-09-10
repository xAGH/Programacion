from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Selenium\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.google.com/?hl=es")

# Abrir nueva pestaña y redirigir a facebook
driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[1])
driver.get("https://www.google.com/?hl=es")
driver.get("https://www.facebook.com/")

# Abrir nueva pestaña y redirigir a Youtube
driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[2])
driver.get("https://www.google.com/?hl=es")
driver.get("https://www.youtube.com/")

# Volver atras en la pestaña
driver.back()

# Cambiar a la segunda pestaña
driver.switch_to_window(driver.window_handles[1])
driver.back()

# Cambiar a la primera pestaña
driver.switch_to_window(driver.window_handles[0])

# Cerramos la primera pestaña(Google)
driver.close()

# Cerramos la segunda pestaña(Facebook)
driver.switch_to_window(driver.window_handles[0])
driver.close()

# Estamos ubicados, como resultado de lo anterior, en la tercera pestaña, la cual es de Youtube, pero que se encuentra en google porque atrasamos la bvusqueda,
# Ahora volvemos de nuevo hacia adelante, es decir, hacia youtube
driver.switch_to_window(driver.window_handles[0])
driver. forward()

driver.quit()