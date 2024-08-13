from selenium.webdriver.common.by import By


class Locators:

    BUTTON_PERSONAL = By.LINK_TEXT, "Личный Кабинет"
    FORM_REGISTRATION = By.CLASS_NAME, "Auth_link__1fOlj"
    INPUT_NAME = By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']"
    INPUT_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    INPUT_PASSWORD = By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль']"
    BUTTON_REGISTRATION = By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"
    BUTTON_LOGO = By.XPATH, '//*[@id="root"]/div/header/nav/div/a'
    BUTTON_ENTER_PAC = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"
    INPUT_AUTORIZATION_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    INPUT_AUTORIZATION_PASS = By.CSS_SELECTOR, "input[name='Пароль']"
    BUTTON_AUTORIZATION_CHECK_IN = By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa"
    BUTTON_CONSTRUCTOR = By.LINK_TEXT, "Конструктор"
    BUTTON_RECOVERY_PASS = By.LINK_TEXT, "Восстановить пароль"
    BUTTON_ACCOUNT = By.CSS_SELECTOR, ".Account_button__14Yp3"
    INC_PASSWORD = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"
    ELEMENT_SAUSE = By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc') and span[text()='Соусы']]"
    ELEMENT_BREAD = By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc') and span[text()='Булки']]"
    ELEMENT_FILLING = By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc') and span[text()='Начинки']]"
    ELEMENT_EXIT = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]"
    ELEMEN_ORDER = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"
    ELEMENT_LOGIN = By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']"
    ELEMENT_ACCOUNT = By.CSS_SELECTOR, ".Account_link__2ETsJ.text.text_type_main-medium.text_color_inactive.Account_link_active__2opc9"
    ELEMENT_EX = By.XPATH, "//h2[text()='Вход']"
    ELEMENT_BURGER = By.XPATH, "//h1[text()='Соберите бургер']"
    BUTTON_EX = By.XPATH, "//button[contains(text(), 'Войти')]"

class Test_burger_constructor:

    BUTTON_SAUCES = By.XPATH, "//span[text()='Соусы']"
    BUTTON_FILLINGS = By.XPATH, "//span[text()='Начинки']"
    BUTTON_BREADS = By.XPATH, "//span[text()='Булки']"

class Test_recovery_form_locators:
    BUTTON_RECOVERY_PASSWORD = By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']"