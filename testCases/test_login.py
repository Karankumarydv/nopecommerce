import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger= LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("************ Test_001_Login*******")
        self.logger.info("************ verifying home Page Title*******")
        self.driver= setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("************home Page Title is passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************home Page Title is failed*******")
            assert False

    def test_login(self,setup):
        self.logger.info("************ verifying login test*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************login test is passed*******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_login.png")
            self.driver.close()
            self.logger.error ("************login test is failed*******")
            assert False
