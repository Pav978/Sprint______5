import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver

from locators import Locators
from constants import Constants


class Test_Personal_to_construktor_logo:
    def test_personal_to_constructor(self, driver):
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
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_EXIT)))
        assert driver.find_element(*Locators.ELEMENT_EXIT).is_displayed(), "Кнопка 'Войти' не отображается после регистрации"
        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (Locators.ELEMEN_ORDER)))
        assert driver.find_element(*Locators.ELEMEN_ORDER).is_displayed(), "Кнопка 'Оформить заказ' не отображается после авторизации"
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_BURGER)))
        assert driver.find_element(*Locators.ELEMENT_BURGER).is_displayed(), "Текст 'Соберите бургер' не отображается на странице конструктора"

    def test_personal_to_logo(self, driver):
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
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_EXIT)))
        assert driver.find_element(*Locators.ELEMENT_EXIT).is_displayed(), "Кнопка 'Войти' не отображается после регистрации"
        driver.find_element(*Locators.INPUT_AUTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*Locators.INPUT_AUTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*Locators.BUTTON_AUTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (Locators.ELEMEN_ORDER)))
        assert driver.find_element(*Locators.ELEMEN_ORDER).is_displayed(), "Кнопка 'Оформить заказ' не отображается после авторизации"
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_LOGO).click()

# Проверка, что переход на главную страницу выполнен успешно
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEMENT_BURGER)))
        assert driver.current_url == Constants.URL, "Переход на главную страницу не выполнен при нажатии на логотип"