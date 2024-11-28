from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)


    def click_cart(self):
        self.click(*self.CART_BTN)