import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer Page   //p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]
    lnkCustomers_menu_xpath = (By.XPATH,"//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]")
    lnkCustomers_menuitem_xpath = (By.XPATH,"(//a[@href='/Admin/Customer/List'])[1]")
    btnAddnew_xpath = (By.XPATH,"(//i[@class='fas fa-plus-square'])[1]")
    txtEmail_xpath = (By.XPATH,"//input[@id='Email']")
    txtPassword_xpath = (By.XPATH,"//input[@id='Password']")
    txtcustomerRoles_xpath = (By.XPATH,"//div[@class='k-multiselect-wrap k-floatwrap']")
    lstitemAdministrators_xpath = (By.XPATH,"//li[contains(text(),'Administrators')]")
    lstitemRegistered_xpath = (By.XPATH,"//li[contains(text(),'Registered')]")
    lstitemGuests_xpath = (By.XPATH,"//li[contains(text(),'Guests')]")
    lstitemVendors_xpath = (By.XPATH,"//li[contains(text(),'Vendors')]")
    drpmgrOfVendor_xpath =(By.XPATH, "//*[@id='VendorId']")
    rdMaleGender_id = (By.ID,"Gender_Male")
    rdFeMaleGender_id = (By.ID,"Gender_Female")
    txtFirstName_xpath = (By.XPATH,"//input[@id='FirstName']")
    txtLastName_xpath = (By.XPATH,"//input[@id='LastName']")
    txtDob_xpath = (By.XPATH,"//input[@id='DateOfBirth']")
    txtCompanyName_xpath = (By.XPATH,"//input[@id='Company']")
    txtAdminContent_xpath = (By.XPATH,"//textarea[@id='AdminComment']")
    btnSave_xpath = (By.XPATH,"//button[@name='save']")


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(*AddCustomer.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(*AddCustomer.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(*AddCustomer.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(*AddCustomer.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(*AddCustomer.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(*AddCustomer.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(*AddCustomer.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(*AddCustomer.lstitemAdministrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(*AddCustomer.lstitemGuests_xpath)
        elif role=='Registered':
            self.listitem = self.driver.find_element(*AddCustomer.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element(*AddCustomer.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(*AddCustomer.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(*AddCustomer.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(*AddCustomer.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(*AddCustomer.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(*AddCustomer.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(*AddCustomer.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(*AddCustomer.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(*AddCustomer.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(*AddCustomer.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(*AddCustomer.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(*AddCustomer.btnSave_xpath).click()