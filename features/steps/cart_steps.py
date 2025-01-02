from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')


@when('Open cart page')
def open_cart(context):
    context.app.main_page.open_cart()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@then('Verify that cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items(amount)


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name(product_name=context.app.cart_page.product_name)
