import random
import string
import pytest
from selenium import webdriver

@pytest.fixture
def driver():  # создание и закрытие драйвера/браузера
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.fixture()  # генерируем логинчик
def login():
    prefix = "best_power_incredible"
    domain = "ru"
    random_number = random.randint(100, 10000)
    login = f"{prefix}@{random_number}.{domain}"
    return login

@pytest.fixture()  # генерируем паролик
def password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password
