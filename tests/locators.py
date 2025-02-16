from selenium.webdriver.common.by import By
class LoginPageLocators():
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//a[@href = '/account']") # кнопка входа в личный кабинет
    SUBMIT_BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") # кнопка входа в аккаунт на главной

class RegistrationPageLocators():
    SUBMIT_BUTTON_REGISTRATION_ACCOUNT = (By.XPATH, ".//form/button[text() = 'Войти']") # кнопка зарегистироваться на странцие регистрации
    SUBMIT_BUTTON_ACCOUNT_RECOVERY = (By.XPATH, ".//form/button[text() = 'Восстановить']") # кнопка восстановления пароля на странице восстановления
    INPUT_NAME_REGISTRATION = (By.XPATH, ".//div/label[text() = 'Имя']") # поле ввода имени на странице регистрации
    INPUT_EMAIL_REGISTRATION = (By.XPATH, ".//div/label[text() = 'Email']") # поле ввода email на странице регистрации
    INPUT_PASSWORD_REGISTRATION = (By.XPATH, ".//div/label[text() = 'Пароль']") # поле ввода пароля на странице регистрации

class ProfilePageLocators():
    pass

class ConstructorPageLocators():
    CONSTRUCTOR_BUTTON = (By.XPATH, './/a[@href="/"]/p') # кнопка перехода на таб с констуктором
    TAB_BUNS = (By.XPATH, ".//section/div[@style = 'display: flex;']/div[1]") # таб булки на главной
    TAB_SAUCES = (By.XPATH, ".//section/div[@style = 'display: flex;']/div[2]")# таб соусы на главной
    TAB_FILLINGS = (By.XPATH, ".//section/div[@style = 'display: flex;']/div[3]")# таб начинки на главной
