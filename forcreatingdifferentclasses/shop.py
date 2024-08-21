import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

class Shop():

    def __init__(self, driver):
        self.driver = driver

    def click_item(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        self.driver.find_element(By.LINK_TEXT, "Shop").click()
        self.driver.find_element(By.XPATH,"(//button[@class='btn btn-info'])[1]").click()



