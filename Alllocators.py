import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select


class Using:
    def __init__(self):
        # Initialize the WebDriver in the constructor
        self.driver = webdriver.Chrome()
        print("mai bap hun mai chl ra hu ")

    def function(self):
        try:


            self.driver.get("https://rahulshettyacademy.com/angularpractice/")
            self.driver.find_element(By.XPATH, "//input[@name='name'][1]").send_keys("abc")
            self.driver.find_element(By.NAME, 'email').send_keys("abc@gmail.com")

            time.sleep(2)
            # Optionally print the title or other actions
            # print(self.driver.title)
        except Exception as e:
            print(e)



    def func(self):
        self.driver.find_element(By.XPATH,'//input[@id="exampleInputPassword1"]').send_keys("abc")
        self.driver.find_element(By.XPATH, "// input[ @ type = 'submit']").click()
        message=self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        #check assertiao
        assert "Success" in message

        #/tagname [@attribute='value'] css same but remove @ and // also one more css selector #id .classname
        # for multiple indexes use index (/tagname [@attribute='value'] )[3]
        #linktext find by text and u can find what is link text it have "a" tag
        #travelling from parent to child is like parent/child/child[2]/[child] if this child have 4 and u need to go on 2
        #we can do this when there is no attribute ike this   //form/div[1]/input
        # for text tagname(text()='save new password') but @ ni aega

        #select basically used in static dropdown
        time.sleep(2)
        selecting=Select(self.driver.find_element(By.ID,'exampleFormControlSelect1'))
        selecting.select_by_index(1)
        #when there is no id class any ting available so we can traverse like this //td/td[5]




        time.sleep(2)





            # Ensure that the browser is closed even if an error occurs


# Create an instance of the Using class
obj = Using()
# Call the function method
obj.function()
obj.func()


#bascially chrome is not give oermission directly to any automation script to invoke so for this there is a middle
#man called chrome driver chrom driver is build with browser version so when ever some one wants to hit chrom first
# work is off chrome driver






#find_elements(By.XPATH, ...) returns a list of WebElements. You cannot call .send_keys() on a list.





 #service it is used to give manually driver version

  #phythin liabrary it make script 2 sec wait