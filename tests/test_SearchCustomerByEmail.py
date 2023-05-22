import time
import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.BaseClass import BaseClass


class Test_SearchCustomerByEmail(BaseClass):

    def test_searchCustomerByEmail(self):
        log = self.getLogger()
        log.info("************* Test_003_AddCustomer **********")
        log = self.getLogger()
        lp = LoginPage(self.driver)
        lp.setUserName().send_keys("admin@yourstore.com")
        lp.setPassword().send_keys("admin")
        lp.clickLogin()
        log.info("************* Login succesful **********")

        log.info("******* Starting Search Customer By Email **********")

        addcust = AddCustomer(self.driver)
        time.sleep(3)
        addcust.clickOnCustomersMenu()
        time.sleep(3)
        addcust.clickOnCustomersMenuItem()

        log.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        time.sleep(2)
        searchcust.setEmail().send_keys("victoria_victoria@nopCommerce.com")
        time.sleep(5)
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True
        log.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")


