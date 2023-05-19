import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.loginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer

from utilities.BaseClass import BaseClass
import string
import random

class Test_003_AddCustomer(BaseClass):
    def test_addCustomer(self):
        log = self.getLogger()
        log.info("************* Test_003_AddCustomer **********")
        log = self.getLogger()
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys("admin@yourstore.com")
        lp.setPassword().send_keys("admin")
        lp.clickLogin()
        log.info("************* Login succesful **********")

        log.info("******* Starting Add Customer Test **********")

        addcust = AddCustomer(self.driver)
        time.sleep(3)
        addcust.clickOnCustomersMenu()
        time.sleep(3)
        addcust.clickOnCustomersMenuItem()
        time.sleep(3)
        addcust.clickOnAddnew()

        log.info("************* Providing customer info **********")

        email = random_generator() + "@gmail.com"
        addcust.setEmail(email)
        addcust.setPassword("test123")
        addcust.setCustomerRoles("Guests")
        addcust.setManagerOfVendor("Vendor 2")
        addcust.setGender("Male")
        addcust.setFirstName("Adarsh")
        addcust.setLastName("singh")
        addcust.setDob("7/11/1995")  # Format: D / MM / YYY
        addcust.setCompanyName("MT")
        addcust.setAdminContent("This is for testing.........")
        addcust.clickOnSave()

        log.info("************* Saving customer info **********")

        log.info("********* Add customer validation started *****************")

        msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(msg)
        if 'customer has been added successfuly.' in msg:
            assert True
            log.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot("C:/PycharmProject/Selenium_practice/reports/screenshot/test_addcustomer.png")  # Screenshot
            log.error("********* Add customer Test Failed ************")
            assert False

        log.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
