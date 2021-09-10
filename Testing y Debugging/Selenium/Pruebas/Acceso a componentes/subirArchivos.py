from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")

boton = driver.find_element_by_id("myFile")
boton.send_keys(r"C:\Users\Alejo Giraldo\Pictures\Fondos\FMA.jpg")
sleep(3)

driver.quit()