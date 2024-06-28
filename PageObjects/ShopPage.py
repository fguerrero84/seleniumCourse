from selenium.webdriver.common.by import By
from PageObjects.ConfirmationPage import ConfirmationPage


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    phones = (By.XPATH, '//div[@class="card h-100"]')
    phoneTitle = (By.XPATH, 'div/h4/a')
    addToCart = (By.XPATH, 'div/button')
    navCheckout = (By.CSS_SELECTOR, 'a[class*="btn-primary"]')
    chbtn = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')
    confchbtn = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')


    def ItemShop(self):
        return self.driver.find_elements(*ShopPage.phones)

    def getphoneTitle(self):
        return self.driver.find_element(*ShopPage.phoneTitle)

    def AddToCart(self):
        return self.driver.find_element(*ShopPage.addToCart)

    def NavChPage(self):
        return self.driver.find_element(*ShopPage.chbtn)

    def confCh(self):
        self.driver.find_element(*ShopPage.confchbtn).click()
        confirmationPage = ConfirmationPage(self.driver)
        return confirmationPage




    # self.driver.find_element(By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()
    # self.driver.find_element(By.ID, 'country').send_keys('ind')
    # time.sleep(5)
    # wait = WebDriverWait(self.driver, 10)
    # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
    # self.driver.find_element(By.LINK_TEXT, 'India').click()
    # self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    # conf_text = self.driver.find_element(By.CSS_SELECTOR, 'div [class = "alert alert-success alert-dismissible"]').text
    # assert 'Success' in conf_text
    # time.sleep(5)