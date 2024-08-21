import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait




@pytest.mark.usefixtures("setup", "logger")
class BaseClass:



    #i make this to use explicit wait where ever i want
     #def test_verifyexplicitwait(self,text):
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.XPATH,text )))

    def selctingstaticdropdown(self,option_text):
        selecting = Select(self.driver.find_element(By.ID, 'exampleFormControlSelect1'))
        selecting.select_by_visible_text(option_text)



