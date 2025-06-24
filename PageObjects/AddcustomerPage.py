import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#Add customer Page
class AddCustomer():
   lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
   lnkCustomers_menuitem_xpath="/html/body/div[3]/aside/div/nav/ul/li[4]/ul/li[1]/a/p"
   btnAddnew_xpath="//a[@class='btn btn-primary']"
   txtEmail_xpath="//input[@name='Email']"
   txtPassword_xpath="//input[@name='Password']"
   txtFirstName_xpath="//input[@name='FirstName']"
   txtLastName_xpath = "//input[@name='LastName']"
   rdMaleGender_id="//input[@id='Gender_Male']"
   rdFemaleGender_id="//input[@id='Gender_Female']"
   txtCompanyName_xpath="//input[@id='Company']"
   txtcustomerRole_xpath="//*[@id='select2-SelectedCustomerRoleIds-results']"
   lstitemAdministrators_xpath="//li[contains(text(),'Administrators')]"
   lstitemForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
   lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
   lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
   lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
   lstitemala_xpath = "//li[contains(text(),'ala')]"
   lstitemrama_xpath = "//li[contains(text(),'rama')]"
   lstitemkk_xpath = "//li[contains(text(),'kk')]"
   txtAdminComments_xpath="//*[@id='AdminComment']"
   btnSave_xpath="//button[@name='save']"
   drpmgrofVendor_xpath="//select[@id='VendorId']"

   def __init__(self,driver):
      self.driver= driver

   def clickonCustomersMenu(self):
      self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

   def clickonCustomersMenuItem(self):
      self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()
   def clickOnAddnew(self):
      self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

   def setEmail(self,Email):
      self.driver.find_element(By.XPATH, self.txtEmail_xpath).click()
   def setPassword(self,Password):
      self.driver.find_element(By.XPATH, self.txtPassword_xpath).click()

   def SetCustomerRoles(self,role):
      self.driver.find_element(By.XPATH, self.txtcustomerRole_xpath).click()
      time.sleep(2)
      if role=='Registered':
         self.listitem=self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
      elif role=='Administrators':
         self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
      elif role=='Guests':
         time.sleep(3)
         self.driver.find_element(By.XPATH, "//*[@id='SelectCustomerRoleIds_taglist']/li/span[2]").click()
         self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
      elif role=='Registered':
         self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
      elif role=='Vendors':
         self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
      elif role=='ala':
         self.listitem = self.driver.find_element(By.XPATH, self.lstitemala_xpath)
      elif role=='rama':
         self.listitem = self.driver.find_element(By.XPATH, self.lstitemrama_xpath)
      elif role=='kk':
         self.listitem = self.driver.find_element(By.XPATH, self.lstitemkk_xpath)
      else:
         self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
         time.sleep(3)

         self.driver.execute_script("argument[0].click();",self.listitem)

   def setManagerOfVendor(self,value):
      drp=Select(self.driver.find_element(By.XPATH,self.drpmgrofVendor_xpath))
      drp.select_by_visible_text(value)
   def setGender(self,gender):
      if gender=='Male':
         self.driver.find_element(By.XPATH,self.rdMaleGender_id).click()
      elif gender=='Female':
         self.driver.find_element(By.XPATH,self.rdFemaleGender_id).click()
      else:
         self.driver.find_element(By.XPATH, self.rdMaleGender_id).click()

   def setFirstName(self,fname):
      self.driver.find_element(By.XPATH, self.txtFirstName_xpath).sendkeys(fname)
   def setLastName(self,lname):
      self.driver.find_element(By.XPATH, self.txtLastName_xpath).sendkeys(lname)
   def setCompanyName(self,comname):
      self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).sendkeys(comname)
   def setAdminContent(self,content):
      self.driver.find_element(By.XPATH, self.txtAdminComments_xpath).sendkeys(content)
   def clickOnSave(self):
      self.driver.find_element(By.XPATH, self.btnSave_xpath).click()












