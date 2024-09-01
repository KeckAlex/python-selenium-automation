from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


CART_TOTAL = (By.CSS_SELECTOR, "[class='h-margin-l-x2']")
# CART_TOTAL = (By.CSS_SELECTOR, "[data-test='cart-summary-subTotal'] [class='h-text-md']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[id*='item-title']") #"[data-test='cart-item-title']")
CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')


@when('Open cart page')
def open_cart(context):
    # context.driver.find_element(By.XPATH, "//a[@href='/cart']").click()
    context.driver.get('https://www.target.com/cart')
    context.driver.wait.until(EC.visibility_of_element_located(CART_ICON))


@then('Verify “Your cart is empty” message is shown')
def cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"] h1').text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}'
    print('Test case passed')



@then('Verify that cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_total = context.driver.find_element(*CART_TOTAL).text
    assert f'{amount} item' in cart_total, f'Expected {amount} not in cart total, but got {cart_total}'


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"
