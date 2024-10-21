from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then, when
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
CONFIRM_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
LISTINGS = (By.CSS_SELECTOR, '[data-test="@web/site-top-of-funnel/ProductCardWrapper"]')
PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="product-title"]')
# PRODUCT_IMAGE = (By.CSS_SELECTOR, '[data-test="product-title"], img')
PRODUCT_IMAGE = (By.CSS_SELECTOR, 'img')

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


@then('Verify Sign In form opened')
def sign_in_opened(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "#__next h1").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}'
    print('Test case passed')


@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_text()


@then('Verify correct search results URL opens for {expected_product}')
def verify_URL(context, expected_product):
    context.app.search_results_page.verify_url()


@then('Verify that user can see product names and images')
def verify_products_name_img(context):
    # To see All listings (comment out if you only check top one)
    sleep(10)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        image = product.find_element(*PRODUCT_IMAGE)
        assert image, 'Product image not shown'