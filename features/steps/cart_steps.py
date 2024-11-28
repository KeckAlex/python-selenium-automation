from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


CART_TOTAL = (By.CSS_SELECTOR, "[class='h-margin-l-x2']")
# CART_TOTAL = (By.CSS_SELECTOR, "[data-test='cart-summary-subTotal'] [class='h-text-md']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[id*='item-title']") #"[data-test='cart-item-title']")
CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@then('Verify that cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_total = context.driver.find_element(*CART_TOTAL).text
    assert f'{amount} item' in cart_total, f'Expected {amount} not in cart total, but got {cart_total}'


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"
