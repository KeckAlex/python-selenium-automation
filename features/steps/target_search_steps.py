from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for product')
def search_product(context):
    # find search field and enter text 'tea'
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)

@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} at in actual text {actual_text}'

@when('Click on Cart icon')
def click_cart_icon(context):
    # find the cart icon and click on it
    context.driver.find_element(By.CSS_SELECTOR, "use[href='/icons/Cart.svg#Cart']").click()
    sleep(3)

@then('Verify “Your cart is empty” message is shown')
def cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "#cart-container h1").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}'

    print('Test case passed')
    context.driver.quit()

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()
    sleep(3)


@when('From right side navigation menu click Sign In')
def click_sign_in_side_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
    sleep(3)


@then('Verify Sign In form opened')
def sign_in_opened(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "#__next h1").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}'

    print('Test case passed')
    context.driver.quit()