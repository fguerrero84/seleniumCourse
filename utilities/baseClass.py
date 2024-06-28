import pytest
import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures('setup')
class baseClass:

    def presenceVerification(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def SelectGender(self, locator, text):
        # selection of the dropdown element for STATIC DROPDOWNs (NOT AUTOCOMPLETING)
        GenderDrop = Select(locator)
        GenderDrop.select_by_visible_text('Male')


    def getLogs(self):
        testName = inspect.stack()[1][3]
        logger = logging.getLogger(testName)
        fileHandler = logging.FileHandler('logfile.log')
        fileFormatter = logging.Formatter('%(asctime)s :%(levelname)s : %(name)s :%(message)s')
        fileHandler.setFormatter(fileFormatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger