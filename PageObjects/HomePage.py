from selenium.webdriver.common.by import By
from PageObjects.ShopPage import ShopPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, 'a[href*="shop"]')
    #below for angularPractice
    name = (By.CSS_SELECTOR, 'input[name="name"]')
    email = (By.NAME, 'email')
    angCB = (By.ID, 'exampleCheck1')
    angRad = (By.CSS_SELECTOR, 'input[id="inlineRadio1"]')
    gender = (By.ID, 'exampleFormControlSelect1')
    submitbtn = (By.XPATH, '//input[@type="submit"]')
    successMsg = (By.CSS_SELECTOR, '[class*="alert-success"]')

    def NavShop(self):
        self.driver.find_element(*HomePage.shop).click()
        shopPage = ShopPage(self.driver)
        return shopPage

    def GetName(self):
        return self.driver.find_element(*HomePage.name)

    def GetEmail(self):
        return self.driver.find_element(*HomePage.email)

    def GetAngCB(self):
        return self.driver.find_element(*HomePage.angCB)

    def GetAngRad(self):
        return self.driver.find_element(*HomePage.angRad)

    def GetGender(self):
        return self.driver.find_element(*HomePage.gender)

    def SubmitForm(self):
        return self.driver.find_element(*HomePage.submitbtn)

    def ConfirmSuccess(self):
        return self.driver.find_element(*HomePage.successMsg)


