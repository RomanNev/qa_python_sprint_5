from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators, ProfilePageLocators, ConstructorPageLocators
import data


class TestProfilePage:

    def test_personal_account_button_redirects_correct(self, driver): # Проверяет переход по клику на «Личный кабинет»
        driver.get(data.URLS["login"])

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(data.TEST_USER["email"])
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys(data.TEST_USER["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        driver.find_element(*LoginPageLocators.BUTTON_PERSONAL_ACCOUNT).click() # клик по кнопке «Личный кабинет»
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((ProfilePageLocators.ACCOUNT_TEXT_IN_PROFILE))) # ждем текст в личном кабинете
        text_account = driver.find_element(*ProfilePageLocators.ACCOUNT_TEXT_IN_PROFILE).text
        assert "В этом разделе вы можете изменить свои персональные данные" == text_account

    def test_navigate_from_personal_account_to_constructor(self, driver): # Проверяет переход по клику на «Конструктор» из личного кабинета
        driver.get(data.URLS["login"])

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(data.TEST_USER["email"])
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys(data.TEST_USER["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        driver.find_element(*LoginPageLocators.BUTTON_PERSONAL_ACCOUNT).click() # клик по кнопке «Личный кабинет»
        driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_BUTTON).click() # клик по кнопке  «Конструктор» из личного кабинета
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((ConstructorPageLocators.CONSTRUCTOR_TITLE)))
        text_title =  driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_TITLE).text
        assert "Соберите бургер" == text_title

    def test_navigate_to_main_page_via_stellar_burgers_logo(self, driver):  # Проверяет переход по клику на логотип Stellar Burgers из личного кабинета
        driver.get(data.URLS["login"])

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(data.TEST_USER["email"])
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys(data.TEST_USER["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()
        driver.find_element(*LoginPageLocators.BUTTON_PERSONAL_ACCOUNT).click()  # переход в «Личный кабинет»

        driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_LOGO).click() # переход из личного кабинета по клику на Stellar Burgers
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((ConstructorPageLocators.CONSTRUCTOR_TITLE)))
        text_title = driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_TITLE).text
        assert "Соберите бургер" == text_title













