from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
SIGN_IN = (By.ID, 'account-sign-in')
LOG_IN = (By.ID, 'logIn')


@given('Open target main page')
def open_target(context):
    context.app.main_page.open()

@given('Open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')

@given('Open sign in page')
def open_sign_in(context):
    context.app.main_page.open_sign_in_page()

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()


@when('Click Sign In')
def click_sign_in(context):
    context.app.main_page.click_signin()


@when('From right side navigation menu click Sign In')
def click_sign_in_side_menu(context):
    context.app.main_page.click_signin_sidenav_btn()


@then('Verify header is shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")


@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'

    for i in range(len(links)):
        links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
        links[i].click()


@then('Verify target circle page has 14 benefit cells')
def verify_header_link_amount(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='cell-item-content']")
    assert len(links) == 14, f'Expected {14} links, but got {len(links)}'



