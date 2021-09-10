from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")

checkbox = driver.find_element_by_xpath("""//*[@id="main"]/div[3]/div[1]/input[2]""")

print(checkbox.is_selected())
print(checkbox.is_enabled())
print(checkbox.is_displayed())

driver.quit()