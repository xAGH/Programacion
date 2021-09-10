from selenium import webdriver as wb
from time import sleep
    
driver = wb.Chrome(executable_path=(r"F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe"))
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F%3Futm_source%3Dadwords-brand%26utm_medium%3Dudemyads%26utm_campaign%3DNEW-AW-PROS-Branded-Search-SP-SPA_._ci__._sl_SPA_._vi__._sd_All_._la_SP_._%26tabei%3D7%26utm_term%3D_._ag_53604040718_._ad_254061738916_._de_c_._dm__._pl__._ti_kwd-310556426868_._li_1003665_._pd__._%26gclid%3DEAIaIQobChMIv4zU1YXz8QIVCbKGCh1q_wasEAAYASAAEgKSAvD_BwE")

usuario = driver.find_element_by_id("email--1")
clave = driver.find_element_by_id("id_password")
enviar = driver.find_element_by_id("submit-id-submit")

usuario.send_keys("alejopruebas23001@gmail.com")
clave.send_keys("alejo12345")

enviar.click()

driver.quit()