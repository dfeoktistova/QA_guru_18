import requests
from model.const import URL
from selene import browser, have
import allure
from allure_commons.types import AttachmentType


def add_product_to_cart(product_id, quantity):
    options = {f'addtocart_{product_id}.EnteredQuantity': {quantity}}
    response = requests.post(URL + f"addproducttocart/details/{product_id}/1", data=options)

    assert response.status_code == 200

    allure.attach(body=response.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
    allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
    allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    return response


def update_cookie(response, is_login: False):
    cookie = response.cookies.get("Nop.customer")

    browser.open(URL + 'cart')
    browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})

    if is_login:
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})

    browser.open(URL + 'cart')


def checking_product_name_in_cart(product_name):
    browser.element('.product-name').should(have.text(product_name))


def checking_product_quantity_in_cart(quantity):
    browser.element('.qty-input').should(have.value(quantity))
