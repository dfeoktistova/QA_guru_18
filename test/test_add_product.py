from pages.cart import *
from data.product import smartphone, notebook
import pytest


@pytest.mark.parametrize("product_id, product_name, quantity",
                         [(smartphone.id, smartphone.name, smartphone.quantity),
                          (notebook.id, notebook.name, notebook.quantity)])
def test_add_product_to_cart_without_authorization(product_id, product_name, quantity):
    with allure.step("Добавить товар в корзину"):
        response = add_product_to_cart(product_id, quantity)

    with allure.step("Обновить куки"):
        update_cookie(response, is_login=False)

    with allure.step("Проверить наличие товара в корзине"):
        checking_product_name_in_cart(product_name)

    with allure.step("Проверить количество товара в корзине"):
        checking_product_quantity_in_cart(quantity)


@pytest.mark.parametrize("product_id, product_name, quantity",
                         [(smartphone.id, smartphone.name, smartphone.quantity),
                          (notebook.id, notebook.name, notebook.quantity)])
def test_add_product_to_cart_with_authorization(fixture_api_authorization, product_id, product_name, quantity):
    with allure.step("Добавить товар в корзину"):
        response = add_product_to_cart(product_id, quantity)

    with allure.step("Обновить куки"):
        update_cookie(response, is_login=True)

    with allure.step("Проверить наличие товара в корзине"):
        checking_product_name_in_cart(product_name)

    with allure.step("Проверить количество товара в корзине"):
        checking_product_quantity_in_cart(quantity)