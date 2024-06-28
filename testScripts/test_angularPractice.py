import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.angularPracticeData import angularPracticeData
from utilities.baseClass import baseClass


class TestAngularPractice(baseClass):

    def test_submitForm(self, dataload):
        log = self.getLogs()
        angularpractice = HomePage(self.driver)
        log.info('first name is ' + dataload['first_name'])
        angularpractice.GetName().send_keys(dataload['first_name'])
        angularpractice.GetEmail().send_keys(dataload['last_name'])
        angularpractice.GetAngCB().click()
        angularpractice.GetAngRad().click()
        self.SelectGender(angularpractice.GetGender(), dataload['gender'])
        angularpractice.SubmitForm().click()
        confirmation = angularpractice.ConfirmSuccess().text
        assert ('Success' in confirmation)
        time.sleep(3)
        self.driver.refresh()

    @pytest.fixture(params=angularPracticeData.excelExtraction('TestCase2'))
    def dataload(self, request):
            return request.param
