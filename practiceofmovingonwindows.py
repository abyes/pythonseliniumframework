import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH,"//body/a").click()
tab=driver.window_handles
driver.switch_to.window(tab[1])
rahul=driver.find_element(By.XPATH,"//p[@class='im-para red']").text
domain = rahul.split('@')[1]
domain1=domain.split(' ')[0]

print(domain1)
driver.close()
driver.switch_to.window(tab[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(domain1)
time.sleep(5)
