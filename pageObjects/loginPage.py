from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    textbox_username_id = (By.NAME,"Email")
    textbox_password_id = (By.ID,"Password")
    button_login_xpath = (By.XPATH,"//button[@type='submit']")
    link_logout_linktext = (By.LINK_TEXT,"Logout")

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self):
        self.driver.find_element(*LoginPage.textbox_username_id).clear()
        return self.driver.find_element(*LoginPage.textbox_username_id)

    def setPassword(self):
        self.driver.find_element(*LoginPage.textbox_password_id).clear()
        return self.driver.find_element(*LoginPage.textbox_password_id)

    def clickLogin(self):
        self.driver.find_element(*LoginPage.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(*LoginPage.link_logout_linktext).click()