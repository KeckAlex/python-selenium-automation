from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")


    def search_product(self, product):
        print('POM layer:', product)
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)


    def click_cart(self):
        self.wait_to_be_clickable(*self.CART_BTN)

    def click_sign_in(self, *locator):
        self.wait_and_click(*self.SIGN_IN).click()