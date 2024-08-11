import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver

from locators import Locators
from constants import Constants


class Test_go_to_Personal_account:
    def test_personal_account(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(
            *Locators.FORM_REGISTRATION).click()
        random_name = f"Pal{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_NAME).send_keys(
            random_name)
        random_email = f"123{random.randint(100, 999)}@ya.ru"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(random_email)
        random_pass = f"Sym{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        assert driver.find_element(By.XPATH,
                                   "//button[contains(text(), 'Войти')]").is_displayed(), "Кнопка 'Войти' не отображается после регистрации"

        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMEN_ORDER)))
        assert driver.find_element(*Locators.ELEMEN_ORDER).is_displayed(), "Кнопка 'Оформить заказ' не отображается после авторизации"


        driver.find_element(*Locators.BUTTON_PERSONAL).click()

        # Проверка, что страница "Личный Кабинет" загружена
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_ACCOUNT)))
        assert driver.find_element(*Locators.ELEMENT_ACCOUNT).is_displayed(), "Не удалось перейти в 'Личный Кабинет'"