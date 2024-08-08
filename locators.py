from selenium.webdriver.common.by import By


class Locators:

    BUTTON_PERSONAL = By.LINK_TEXT, "Личный Кабинет"
    FORM_REGISTRATION = By.CLASS_NAME, "Auth_link__1fOlj"
    INPUT_NAME = By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']"
    INPUT_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    INPUT_PASSWORD = By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль']"
    BUTTON_REGISTRATION = By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"
    BUTTON_LOGO = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"
    BUTTON_ENTER_PAC = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"
    INPUT_AUTORIZATION_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    INPUT_AUTORIZATION_PASS = By.CSS_SELECTOR, "input[name='Пароль']"
    BUTTON_AUTORIZATION_CHECK_IN = By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa"
    BUTTON_CONSTRUCTOR = By.LINK_TEXT, "Конструктор"

class Test_burger_constructor:

    BUTTON_SAUCES = By.XPATH, "//span[text()='Соусы']"
    BUTTON_FILLINGS = By.XPATH, "//span[text()='Начинки']"
    BUTTON_BREADS = By.XPATH, "//span[text()='Булки']"

class Test_recovery_form_locators:
    BUTTON_RECOVERY_PASSWORD = By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']"