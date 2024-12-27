from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TXT = (By.CSS_SELECTOR, "#__next h1").text
    SIGN_IN = (By.ID, 'account-sign-in')

    def sign_in_opened(self):
        # expected_text = 'Sign into your Target account'
        # actual_text = context.driver.find_element(SIGN_IN_TXT).text
        # print(actual_text)
        # assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}'
        # print('Test case passed')
        self.wait_for_element_appear(*self.SIGN_IN_TXT)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_TXT)