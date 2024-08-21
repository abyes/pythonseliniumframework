import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys("cu")
time.sleep(2)  #here i give normal wait because implicit wait is not work on findelements because if it return empty list it is not exception like wait until the items load
product=driver.find_elements(By.XPATH,"//div[@class='products']/div")
for products in product:
    products.find_element(By.XPATH,"div/button").click()
    #basically it is traversing like i join parent and child xpath not write the whole one
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']"))).send_keys("rahulshettyacademy")

#driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
#driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()

wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[@class='promoBtn']"))).click()
time.sleep(10)
total=driver.find_elements(By.XPATH,"//tbody/tr/td[5]")
b=0
for totals in total:
    b=int(totals.text) + b
print(b)
amount=driver.find_element(By.XPATH,"//span[@class='totAmt']").text
assert b==int(amount) ,"Assertion fail c"
print('Assertion pass')
TotalAfterDiscount=driver.find_element(By.XPATH,"//span[@class='discountAmt']").text
float(TotalAfterDiscount)
print(TotalAfterDiscount)
assert float(TotalAfterDiscount) < float(b),"assertion fail "
print('assertion pass yahoo')
#explicit wait is used when we know that a specificic item wait for 10 seconds so we define that specifically in
#explicit wait
#until is used for explicit wait



