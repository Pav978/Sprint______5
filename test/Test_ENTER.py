import random
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver

from locators import Locators
from locators import Test_recovery_form_locators


class Test_Enter_In_Page:
    def test_enter_on_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
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
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        time.sleep(6)

        driver.find_element(*Locators.BUTTON_LOGO).click()
        driver.find_element(*Locators.BUTTON_ENTER_PAC).click()

        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))

    def test_enter_in_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
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
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        driver.find_element(*Locators.BUTTON_LOGO).click()
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(
            random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))

    def test_enter_in_Registration_Form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
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
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))

    def test_enter_Recovery_Password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
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
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']")))

        driver.find_element(*Test_recovery_form_locators.BUTTON_RECOVERY_PASSWORD).click()
        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))

