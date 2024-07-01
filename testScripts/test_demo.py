import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.baseClass import baseClass
from PageObjects.HomePage import HomePage
from PageObjects.ShopPage import ShopPage
class Testpy(baseClass):

    def test_phoneE2E(self):
        homePage = HomePage(self.driver)
        shopPage = homePage.NavShop()
        self.driver.implicitly_wait(5)

        # look for the blackberry item
        #shopPage = ShopPage(self.driver)
        #shopPage.ItemShop().click()
        phones = shopPage.ItemShop()
        for phone in phones:
            phoneName = phone.text
            if phoneName == 'Blackberry':
                shopPage.getphoneTitle().click()
                #phone.find_element(By.XPATH, 'div/button').click()

        # add to cart
        #shopPage.addToCart().click()
        #addItem = ShopPage.addToCart()
        self.driver.find_element(By.CSS_SELECTOR, 'a[class*="btn-primary"]').click()

        # checkout procedures
        confirmationPage = shopPage.confCh()
        #self.driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-success"]').click()
        self.driver.find_element(By.ID, 'country').send_keys('ind')
        time.sleep(5)
        self.presenceVerification('India')
        self.driver.find_element(By.LINK_TEXT, 'India').click()
        self.driver.find_element(By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        conf_text = self.driver.find_element(By.CSS_SELECTOR,'div [class = "alert alert-success alert-dismissible"]').text
        assert 'Success' in conf_text
        time.sleep(5)