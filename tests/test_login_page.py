from locators import LoginPageLocators, RegistrationPageLocators, ConstructorPageLocators, ForgotPasswordLocators


class TestLoginPage:

    def test_login_from_main_page_via_login_button(self,
                                                   driver):  # Проверяет вход по кнопке «Войти в аккаунт» на главной
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT_MAIN_PAGE).click() # клик на кнопку «Войти в аккаунт»

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys('romangolubcl_18@yandex.ru')
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys('jKRqvxph')
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        text_button = driver.find_element(*ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER).text
        assert 'Оформить заказ' == text_button

    def test_login_via_personal_account_button(self, driver):  # Проверяет вход через кнопку «Личный кабинет»
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*LoginPageLocators.BUTTON_PERSONAL_ACCOUNT).click() # клик на кнопку «Личный кабинет»

        #авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys('romangolubcl_18@yandex.ru')
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys('jKRqvxph')
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        text_button = driver.find_element(*ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER).text
        assert 'Оформить заказ' == text_button

    def test_login_via_registration_form_button(self, driver):  # Проверяет вход через кнопку войти в форме регистрации
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON_REGISTRATION_FORM).click() # кнопка "войти" в форме регистрации

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys('romangolubcl_18@yandex.ru')
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys('jKRqvxph')
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        text_button = driver.find_element(*ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER).text
        assert 'Оформить заказ' == text_button

    def test_login_via_password_recovery_form_button(self,
                                                     driver):  # Проверяет вход через кнопку в форме восстановления пароля
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*ForgotPasswordLocators.SUBMIT_BUTTON_FORGOT_FORM).click() # кнопка "войти" в форме восстановления пароля

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys('romangolubcl_18@yandex.ru')
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys('jKRqvxph')
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        text_button = driver.find_element(*ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER).text
        assert 'Оформить заказ' == text_button

    def test_logout_button_in_personal_account(self, driver): # проверяет выход по кнопке «Выйти» в личном кабинете
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys('romangolubcl_18@yandex.ru')
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys('jKRqvxph')
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        driver.find_element(*LoginPageLocators.BUTTON_PERSONAL_ACCOUNT).click() # клик по кнопке «Личный кабинет»
        driver.find_element(*LoginPageLocators.BUTTON_LOGOUT_ACCOUNT).click()

        text_button = driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).text
        assert "Войти" == text_button



