import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys('ind')
time.sleep(2)
#country=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
country=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
for countries in country:
    if countries.text == 'India':
        countries.click()
        time.sleep(2)
        #print(driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value"))
        assert (driver.find_element(By.XPATH, "//input[@id='autosuggest']").is_displayed())
        #print( driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value") ==("India"))
        #above statement can give the result for true and false
        break


#for static value that is alreday define on website we use get text method but for the values which are update
#dynamically for this we use get attribute(value)











