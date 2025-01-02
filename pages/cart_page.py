from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CartPage(Page):
    CART_TOTAL = (By.CSS_SELECTOR, "[class='h-margin-l-x2']")
    CART_EMPTY_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

    def __init__(self, driver):
        super().__init__(driver)
        self.product_name = None

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_TXT)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_TXT)

    def verify_product_name(self, product_name):
        actual_name = self.driver.find_element(*self.CART_ITEM_TITLE).text
        assert self.product_name in actual_name, f'Expected {product_name} did not match actual {actual_name}'

    def verify_cart_items(self, amount):
        cart_summary = self.driver.find_element(*self.CART_SUMMARY).text
        assert f'{amount} item in cart_summary, f"Expected {amount} items but got {cart_summary}'

    def click_add_to_cart(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN)).click()   # always clicks on 1st Add to cart btn

        # self.driver.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.driver.wait.until(EC.visibility_of_element_located(self.SIDE_NAV_PRODUCT_NAME))

    def store_product_name(self):
        self.product_name = self.driver.find_element(*self.SIDE_NAV_PRODUCT_NAME).text
        print(f'Stored product name: {self.product_name}')

