import time

from selenium import webdriver

from Alllocators import Using


class Checkbox(Using):
    def __init__(self):
        # Initialize the WebDriver directly in the child class
        self.driver = webdriver.Chrome()
        print("mai beta hu mai bi chl ra hu  ")

    def checkb(self):
        try:
            self.driver.get("https://rahulshettyacademy.com/angularpractice/")
            self.driver.find_element(By.XPATH, '//input[@id="exampleCheck1"]').click()
            time.sleep(2)
        except Exception as g:
            print(f"Error in checkb: {g}")
          # Ensure the browser is closed after operation

# Create an instance of the Checkbox class and perform actions
check = Checkbox()

check.checkb()  #