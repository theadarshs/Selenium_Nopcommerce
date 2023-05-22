from selenium.webdriver.common.by import By


class SearchCustomer():
    # Add customer Page
    Email= (By.ID,"SearchEmail")
    FirstName = (By.ID,"SearchFirstName")
    LastName = (By.ID,"SearchLastName")
    btnSearch = (By.ID,"search-customers")
    tblSearchResults = (By.XPATH,"//table[@role='grid']")
    table = (By.XPATH,"//table[@id='customers-grid']")
    tableRows = (By.XPATH,"//table[@id='customers-grid']//tbody/tr")
    tableColumns = (By.XPATH,"//table[@id='customers-grid']//tbody/tr/td")

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self):
        self.driver.find_element(*SearchCustomer.Email).clear()
        return self.driver.find_element(*SearchCustomer.Email)

    def setFirstName(self):
        self.driver.find_element(*SearchCustomer.FirstName).clear()
        return self.driver.find_element(*SearchCustomer.FirstName)

    def setLastName(self):
        self.driver.find_element(*SearchCustomer.LastName).clear()
        return self.driver.find_element(*SearchCustomer.LastName)

    def clickSearch(self):
        self.driver.find_element(*SearchCustomer.btnSearch).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(*SearchCustomer.tableRows))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(*SearchCustomer.tableColumns))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element(*SearchCustomer.table)
          print("adarsh")
          emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element(*SearchCustomer.table)
          name=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
          if name == Name:
              flag = True
              break
        return flag


