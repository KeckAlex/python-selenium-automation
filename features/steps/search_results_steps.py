from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then, when
from time import sleep


LISTINGS = (By.CSS_SELECTOR, '[data-test="@web/site-top-of-funnel/ProductCardWrapper"]')
PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="product-title"]')
# PRODUCT_IMAGE = (By.CSS_SELECTOR, '[data-test="product-title"], img')
PRODUCT_IMAGE = (By.CSS_SELECTOR, 'img')

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.app.cart_page.click_add_to_cart()


@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    context.app.search_results_page.confirm_add_to_cart()


@when('Store product name')
def store_product_name(context):
    context.app.cart_page.store_product_name()


@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)


@then('Verify correct search results URL opens for {expected_product}')
def verify_URL(context, expected_product):
    context.app.search_results_page.verify_product_in_url(expected_product)


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