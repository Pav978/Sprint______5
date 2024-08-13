import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver

from locators import Locators
from constants import Constants

class Test_exit_Perconall_account:
    def test_exit_perconall_account(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(
            *Locators.FORM_REGISTRATION).click()
        random_name = f"Pal{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_NAME).send_keys(
            random_name)
        random_email = f"123{random.randint(100, 999)}@ya.ru"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(random_email)
        random_pass = f"Pass{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_EXIT)))
        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (Locators.ELEMEN_ORDER)))
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_EX)))