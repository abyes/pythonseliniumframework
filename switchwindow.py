from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
names=driver.window_handles
driver.switch_to.window(names[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()