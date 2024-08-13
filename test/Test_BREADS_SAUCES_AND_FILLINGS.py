from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver

from locators import Test_burger_constructor
from constants import Constants
from locators import Locators

class Test_breads_sauces_fillings:
    def test_constructor_to_sauces(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Test_burger_constructor.BUTTON_SAUCES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_SAUSE)))


    def test_constructor_to_breads(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Test_burger_constructor.BUTTON_FILLINGS).click()
        driver.find_element(*Test_burger_constructor.BUTTON_BREADS).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_BREAD)))
    def test_constructor_to_fillings(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Test_burger_constructor.BUTTON_FILLINGS).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_FILLING)))