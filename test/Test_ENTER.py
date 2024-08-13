import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver

from locators import Locators
from locators import Test_recovery_form_locators
from constants import Constants


class Test_Enter_In_Page:
    def test_enter_on_main_page(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(
            *Locators.FORM_REGISTRATION).click()
        name = "Pal"
        driver.find_element(*Locators.INPUT_NAME).send_keys(
            name)
        random_email = f"123{random.randint(100, 999)}@ya.ru"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(
            random_email)
        random_pass = f"Sym{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(
            random_pass)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_EXIT)))

        driver.find_element(*Locators.BUTTON_LOGO).click()
        driver.find_element(*Locators.BUTTON_ENTER_PAC).click()

        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (Locators.ELEMEN_ORDER)))

    def test_enter_in_personal_account(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(
            *Locators.FORM_REGISTRATION).click()
        random_name = f"Pal_{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_NAME).send_keys(
            random_name)
        random_email = f"123{random.randint(100, 999)}@ya.ru"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(
            random_email)
        random_pass = f"Sym{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(
            random_pass)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_EXIT)))
        driver.find_element(*Locators.BUTTON_LOGO).click()
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(
            random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (Locators.ELEMEN_ORDER)))

    def test_enter_in_Registration_Form(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(
            *Locators.FORM_REGISTRATION).click()
        random_name = f"Pal_{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_NAME).send_keys(
            random_name)
        random_email = f"123{random.randint(100, 999)}@ya.ru"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(random_email)
        random_pass = f"Sym{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_EXIT)))
        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (Locators.ELEMEN_ORDER)))

    def test_enter_Recovery_Password(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(*Locators.FORM_REGISTRATION).click()
        random_name = f"Pal_{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_NAME).send_keys(
            random_name)
        random_email = f"123{random.randint(100, 999)}@ya.ru"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(random_email)
        random_pass = f"Sym{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_EXIT)))
        driver.find_element(*Locators.BUTTON_RECOVERY_PASS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_LOGIN)))

        driver.find_element(*Test_recovery_form_locators.BUTTON_RECOVERY_PASSWORD).click()
        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (Locators.ELEMEN_ORDER)))

