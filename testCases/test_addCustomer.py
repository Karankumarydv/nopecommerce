import random
import string

from selenium.webdriver.common.by import By

from PageObjects.AddcustomerPage import AddCustomer
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
  baseURL= ReadConfig.getApplicationURL()
  username= ReadConfig.getUsername()
  password=ReadConfig.getPassword()
  logger= LogGen.loggen()

  def test_addCustomer(self,setup):
      self.logger.info("************ Test_003_AddCustomer*******")
      self.driver=setup
      self.driver.get(self.baseURL)
      self.driver.maximize_window()

      self.lp = LoginPage(self.driver)
      self.lp.setUserName(self.username)
      self.lp.setPassword(self.password)
      self.lp.ClickLogin()
      self.logger.info("************login is successful *******")
      self.logger.info("************starting add customer test *******")

      self.addcust=AddCustomer(self.driver)
      self.addcust.clickonCustomersMenu()
      self.addcust.clickonCustomersMenuItem()
      self.addcust.clickOnAddnew()

      self.logger.info("************Providing customer info *******")
      self.email = random_generator() +"@gmail.com"
      self.addcust.setEmail(self.email)
      self.addcust.setPassword("test123")
      self.addcust.SetCustomerRoles("Guests")
      self.addcust.setManagerOfVendor("Vendor 2")
      self.addcust.setGender("Male")
      self.addcust.setFirstName("karan")
      self.addcust.setLastName("kumar")
      self.addcust.setCompanyName("busyQA")
      self.addcust.setAdminContent("This is for testing")
      self.addcust.clickOnSave()

      self.logger.info("************Saving customer info *******")

      self.logger.info("************Add customer validation started *******")
      self.msg=self.driver.find_element(By.TAG_NAME,"body").text
      print(self.msg)
      if 'customer has been added successfully.' in self.msg:
        assert True==True
        self.logger.info("************Add customer test passed *******")
      else:
        self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
        self.logger.info("************Add customer test failed *******")
        assert True== False
      self.driver.close()
      self.logger.info("************Ending home page title *******")


def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))


