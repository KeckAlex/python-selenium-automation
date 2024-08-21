from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@given('Open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()



@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "use[href='/icons/Cart.svg#Cart']").click()
    sleep(3)


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()
    sleep(3)


@when('From right side navigation menu click Sign In')
def click_sign_in_side_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
    sleep(3)


@then('Verify header is shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")


@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*=utilityNav]")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'


@then('Verify target circle page has 10 benefit cells')
def verify_header_link_amount(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='cell-item-content']")
    assert len(links) == 10, f'Expected {10} links, but got {len(links)}'

