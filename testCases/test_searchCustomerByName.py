import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.AddcustomerPage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger= LogGen.loggen()

    def test_searchCustomerByName(self,setup):
        self.logger.info("************ SearchCustomerByName_005*******")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("************login is successful *******")
        self.logger.info("************starting search customer By Name *******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clickonCustomersMenuItem()

        self.logger.info("************ searching customer By Name *******")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("Arthur")
        searchcust.setLastName("Holmes")
        searchcust.ClickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Arthur Holmes")
        assert True== status
        self.logger.info("************ TC_searchingCustomerByName_005 finished *******")
        self.driver.close()