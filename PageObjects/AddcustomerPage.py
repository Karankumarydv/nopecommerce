from selenium.webdriver.common.by import By


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




