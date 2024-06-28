from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    CBtc = (By.CSS_SELECTOR, '//div[@class="checkbox checkbox-primary"]')
    DelLoc = (By.ID, 'country')
    purchasebtn = (By.XPATH, '//input[@type="submit"]')
    location = (By.LINK_TEXT,'India')
    confmsg = (By.CSS_SELECTOR, 'div [class = "alert alert-success alert-dismissible"]')

    def markCB(self):
        return self.driver.find_element(*ConfirmationPage.CBtc)

    def sendLoc(self):
        return self.driver.find_element(*ConfirmationPage.DelLoc)

    def selectLoc(self):
        return self.driver.find_element(*ConfirmationPage.location)

    def purchase(self):
        return self.driver.find_element(*ConfirmationPage.purchasebtn)