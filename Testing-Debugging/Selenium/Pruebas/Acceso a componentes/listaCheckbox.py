from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\Programacion\Testing y Debugging\Pruebas Testing\Pruebas\Drivers\chromedriver.exe")
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")

checkbox = driver.find_elements_by_xpath("""//input[@type='checkbox']""")

for checked in checkbox:
    if checked.is_displayed() is True and checked.is_selected() is False:
        checked.click()

driver.quit()