from selenium.webdriver.common.by import By
from behave import given, when, then

CART_TOTAL = (By.CSS_SELECTOR, "[data-test='cart-summary-subTotal']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cart-item-title']")


@when('Open cart page')
def open_cart(context):
    context.driver.find_element(By.XPATH, "//a[@href='/cart']").click()


@then('Verify “Your cart is empty” message is shown')
def cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"] h1').text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}'

    print('Test case passed')
    context.driver.quit()


@then('Verify that cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_total = context.driver.find_element(*CART_TOTAL).text
    assert str(amount) in cart_total, f'Expected {amount} not in cart total, but got {cart_total}'



@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"