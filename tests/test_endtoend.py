import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from forcreatingdifferentclasses.Homepagedata import Homepage_Data
from forcreatingdifferentclasses.checkout import Checkout
from forcreatingdifferentclasses.shop import Shop
from utilities.baseclass import BaseClass

class TestOne(BaseClass):


    def test_one(self, getdata, logger):
        logger.info("Starting test_one")
        logger.info(f"Entering firstname: {getdata['firstname']}")
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys(getdata["firstname"])

        logger.info(f"Selecting gender: {getdata['gender']}")
        self.selctingstaticdropdown(getdata["gender"])

        self.driver.refresh()



    @pytest.fixture(params=Homepage_Data.homepage_var)
    def getdata(self, request):
        return request.param

    def test_two(self, logger):
        logger.info("Starting test_two")
        shop = Shop(self.driver)
        shop.click_item()
        logger.info("Completed test_two")

    def test_three(self, logger):
        logger.info("Starting test_three")
        check = Checkout(self.driver)
        check.Clickoncheckout()
        time.sleep(5)
        logger.info("Completed test_three")
