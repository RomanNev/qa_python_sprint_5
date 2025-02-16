from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//a[@href = '/account']")  # кнопка входа в личный кабинет
    SUBMIT_BUTTON_LOGIN_TO_ACCOUNT_MAIN_PAGE = (
    By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # кнопка входа в аккаунт на главной
    SUBMIT_BUTTON_LOGIN_TO_ACCOUNT = (
    By.XPATH, ".//button[text() = 'Войти']")  # кнопка входа в аккаунт на странице входа
    INPUT_EMAIL_LOGIN = (By.XPATH, ".//input[@name='name']")  # поле ввода имени на странице регистрации
    INPUT_PASSWORD_LOGIN = (By.XPATH, ".//input[@name='Пароль']")  # поле ввода email на странице регистрации
    BUTTON_LOGOUT_ACCOUNT  = (By.XPATH, ".//ul/li[3]/button")  # кнопка выхода из аккаунта в личном кабинете


class RegistrationPageLocators:
    SUBMIT_BUTTON_REGISTRATION_ACCOUNT = (
    By.XPATH, ".//form/button[text() = 'Зарегистрироваться']")  # кнопка зарегистироваться на странцие регистрации
    SUBMIT_BUTTON_ACCOUNT_RECOVERY = (
    By.XPATH, ".//form/button[text() = 'Восстановить']")  # кнопка восстановления пароля на странице восстановления
    INPUT_NAME_REGISTRATION = (
    By.XPATH, ".//form/fieldset[1]/div/div/input")  # поле ввода имени на странице регистрации
    INPUT_EMAIL_REGISTRATION = (
    By.XPATH, ".//form/fieldset[2]/div/div/input")  # поле ввода email на странице регистрации
    INPUT_PASSWORD_REGISTRATION = (
    By.XPATH, ".//form/fieldset[3]/div/div/input")  # поле ввода пароля на странице регистрации
    TEXT_ERROR_PASSWORD_INPUT = (By.XPATH,
                                 ".//p[@class = 'input__error text_type_main-default']")  # сообщение о неккоректном пароле на странице регистрации
    SUBMIT_BUTTON_REGISTRATION_FORM = (
    By.XPATH, ".//p[text() = 'Уже зарегистрированы?']/a")  # Кнопка войти в форме регистрации


class ForgotPasswordLocators:
    SUBMIT_BUTTON_FORGOT_FORM = (
    By.XPATH, ".//p[text() = 'Вспомнили пароль?']/a")  # Кнопка войти в форме восстановления пароля


class ProfilePageLocators:
    ACCOUNT_TEXT_IN_PROFILE = (By.XPATH, ".//p[contains(@class, 'Account_text')]") # текст на странице профиля


class ConstructorPageLocators:
    SUBMIT_BUTTON_PLACE_AN_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    CONSTRUCTOR_BUTTON = (By.XPATH, './/a[@href="/"]/p')  # кнопка перехода на страницу с конструктором
    TAB_BUNS = (By.XPATH, ".//section/div[@style = 'display: flex;']/div[1]")  # таб булки на главной
    TAB_SAUCES = (By.XPATH, ".//section/div[@style = 'display: flex;']/div[2]")  # таб соусы на главной
    TAB_FILLINGS = (By.XPATH, ".//section/div[@style = 'display: flex;']/div[3]")  # таб начинки на главной
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[contains(@class, 'text')]")
    CONSTRUCTOR_LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")


