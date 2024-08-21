import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

Chrome_driver=webdriver.ChromeOptions()

driver=webdriver.Chrome()
driver.implicitly_wait(5)
array=[]

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//div/nav/ul/li[2]").click()
wholebox=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for whole in wholebox:
    productname=whole.find_element(By.XPATH,"div/h4/a[1]").text
    print(productname)
    if productname=="Blackberry":
        whole.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("in")
#wait=WebDriverWait(driver,10)
#wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li")))
time.sleep(5)
table=driver.find_elements(By.XPATH,"//div[@class='suggestions']/ul/li")
for tables in table:
    tab=tables.text

    if tab=="India":
        tables.click()
        break

time.sleep(5)


#print(array)

