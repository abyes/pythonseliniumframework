from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class Checkout():


    def __init__(self,driver):
        self.driver=driver

    def Clickoncheckout(self):
        self.driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()






