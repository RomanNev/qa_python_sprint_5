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


