from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    CONFIRM_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")


    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)

    def confirm_add_to_cart(self):
        self.driver.find_element(*self.CONFIRM_ADD_TO_CART).click()
