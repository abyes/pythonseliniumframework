

from selenium import webdriver
from selenium.webdriver.common.by import By

chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument("==Start-maximized")
#chromeoptions.add_argument("headless")
chromeoptions.add_argument("--ignore-certificate-errors")
driver=webdriver.Chrome(options=chromeoptions)
driver.implicitly_wait(5)
sortedveggies=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
orignallistbybrow=driver.find_elements(By.XPATH,"//tr/td[1]")
for orignal in orignallistbybrow:
    sortedveggies.append(orignal.text)
print(sortedveggies)
orignalbrowsersortedlist=sortedveggies.copy()
sortedveggies.sort()
assert orignalbrowsersortedlist ==sortedveggies,"its fail"
print("Assertion pass bro")

