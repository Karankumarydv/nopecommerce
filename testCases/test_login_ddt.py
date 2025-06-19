import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test_002_DDT_Login:
    baseURL= ReadConfig.getApplicationURL()
    path=".//TestData/loginData.xlsx"
    logger= LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("************Test_002_DDT_Login*******")
        self.logger.info("************ verifying login DDT_test*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in a excel",self.rows)
        lst_status=[] # empty list variable
        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
              if self.exp=='Pass':
               self.logger.info("******passed******")
               self.lp.ClickLogout()
               lst_status.append("pass")
              elif self.exp=='Fail':
                  self.logger.info("******failed******")
                  self.lp.ClickLogout()
                  lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=='Pass':
                    self.logger.info("*****failed***")
                    lst_status.append("Fail")
                elif self.exp=='Fail':
                    self.logger.info("***passed***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
          self.logger.info("****Login DDT test passed ******")
          self.driver.close()
          assert True
        else:
           self.logger.info("****Login DDT test failed ******")
           self.driver.close()
           assert False

