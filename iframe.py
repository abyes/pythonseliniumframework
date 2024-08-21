from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from practiceofmovingonwindows import tab

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame('mce_0_ifr')
wait= WebDriverWait(driver,10)

element = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//body[@id='tinymce']")))
text = element.text
print(text)
driver.switch_to.default_content()

save=driver.find_element(By.XPATH,"//div/h3").text
print(save)


