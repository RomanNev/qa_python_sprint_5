from locators import LoginPageLocators, ProfilePageLocators, ConstructorPageLocators


class TestProfilePage:

    def test_personal_account_button_redirects_correct(self, driver): # Проверяет переход по клику на «Личный кабинет»
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys('romangolubcl_18@yandex.ru')
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys('jKRqvxph')
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        driver.find_element(*LoginPageLocators.BUTTON_PERSONAL_ACCOUNT).click() # клик по кнопке «Личный кабинет»

        text_account = driver.find_element(*ProfilePageLocators.ACCOUNT_TEXT_IN_PROFILE).text
        assert "В этом разделе вы можете изменить свои персональные данные" == text_account

    def test_navigate_from_personal_account_to_constructor(self, driver): # Проверяет переход по клику на «Конструктор» из личного кабинета
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys('romangolubcl_18@yandex.ru')
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys('jKRqvxph')
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()
        driver.find_element(*LoginPageLocators.BUTTON_PERSONAL_ACCOUNT).click() # клик по кнопке «Личный кабинет»

        driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_BUTTON).click() # клик по кнопке  «Конструктор» из личного кабинета
        text_title =  driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_TITLE).text
        assert "Соберите бургер" == text_title

    def test_navigate_to_main_page_via_stellar_burgers_logo(self, driver):  # Проверяет переход по клику на логотип Stellar Burgers из личного кабинета
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys('romangolubcl_18@yandex.ru')
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys('jKRqvxph')
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()
        driver.find_element(*LoginPageLocators.BUTTON_PERSONAL_ACCOUNT).click()  # переход в «Личный кабинет»

        driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_LOGO).click() # переход из личного кабинета по клику на Stellar Burgers
        text_title = driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_TITLE).text
        assert "Соберите бургер" == text_title














