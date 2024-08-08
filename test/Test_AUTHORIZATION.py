import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver
from locators import Locators


class Test_Authorization:
    def test_authorization(self, driver):
#Заходим на страницу бургерной
        driver.get("https://stellarburgers.nomoreparties.site/")
#Переход в ЛК
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
#Переход к регистрации
        driver.find_element(*Locators.FORM_REGISTRATION).click()
#Ввод имени, email и пароля
        random_name = f"Pal_{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_NAME).send_keys(
            random_name)
        random_email = f"123{random.randint(100, 999)}@ya.ru"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(random_email)
        random_pass = f"{random.randint(100, 999)}"
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(random_pass)
#Нажимаем зарегистрироваться
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")))
#Проверка правильности пароля
        error_message = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")))
        assert error_message.is_displayed()

