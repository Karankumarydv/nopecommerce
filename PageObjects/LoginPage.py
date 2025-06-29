from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id="Email"
    textbox_password_id = "Password"
    button_login_Xpath="//button[@type='submit']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):

        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self, Password):
            self.driver.find_element(By.ID,self.textbox_password_id).clear()
            self.driver.find_element(By.ID,self.textbox_password_id).send_keys(Password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_Xpath).click()

    def ClickLogout(self):
            self.driver.find_element(By.XPATH,self.link_logout_linktext).click()


