import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
#checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("id") == "checkBoxOption2":
        checkbox.click()
        time.sleep(2)
        assert checkbox.is_selected()
#alerts , popup ,java alrets popup alerts for this one u have to switch from browser to alert mode

name="abyes"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
popup=driver.switch_to.alert


print(popup.text)
assert name in popup.text
popup.accept()


