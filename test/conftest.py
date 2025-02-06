import time

import pytest
from selene import browser, have
from selenium import webdriver
from model.const import *
import allure
import requests
import logging


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    browser.open(URL)

    yield

    browser.quit()


@pytest.fixture()
def fixture_api_authorization():
    with allure.step("Авторизоваться через API"):
        response = requests.post(
            url=URL + "login",
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False)

    with allure.step('Обновить куки'):
        authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

        browser.open(URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
        browser.open(URL)

    with allure.step("Проверка авторизации"):
        browser.element(".account").should(have.text(LOGIN))

    return authorization_cookie


@pytest.fixture(scope='function', autouse=True)
def delete_all_cookies():
    yield

    with allure.step('Очистить куки'):
        browser.open(URL)
        browser.driver.delete_all_cookies()
        browser.open(URL)

        time.sleep(2)