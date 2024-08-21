from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
#headless bi use kr skte hain hum chrome_option_add argument krke
#or akssar website pe jo security ajati hai usko ignore bi kr skte hain by upar wali chez likh kr phr --ignore-certificate-error likh kr 
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#it move to the specific height window.scrollBy(0,500)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("matlabi.png")