from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then, when
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
CONFIRM_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    sleep(5)
    context.driver.execute_script("window.scrollTo(0, 500)")
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()   # always clicks on 1st Add to cart btn

    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='addToCartButton']")[0].click()
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))


@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    context.driver.find_element(*CONFIRM_ADD_TO_CART).click()
    sleep(6)


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Stored product name: {context.product_name}')


@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    print(actual_text)
    assert product in actual_text, f'Expected text {product} at in actual text {actual_text}'


@then('Verify Sign In form opened')
def sign_in_opened(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "#__next h1").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}'
    print('Test case passed')



@then('Verify search results URL opens for {expected_product}')
def verify_URL(context, expected_product):
    url = context.driver.current_url
    assert expected_product in url, f'Expected {expected_product}' not in{url}


