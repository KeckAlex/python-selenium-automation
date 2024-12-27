from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TXT = (By.CSS_SELECTOR, "#__next h1")
    SIGN_IN = (By.ID, 'account-sign-in')

    def sign_in_opened(self):
        self.wait_for_element_appear(*self.SIGN_IN_TXT)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_TXT)