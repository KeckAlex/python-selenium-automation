from selenium.webdriver.common.by import By

from homework_target import actual_text
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TXT = (By.CSS_SELECTOR, "#__next h1")
    SIGN_IN = (By.ID, 'account-sign-in')
    EMAIL_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    EMAIL = 'lochoa0929@fkmalozmpclf.cfd'
    PASSWORD = 'Abra1122D'
    LOG_IN = (By.ID, 'login')
    ALERT = (By.CSS_SELECTOR, '[data-test="authAlertDisplay"]')
    TEXT = 'find your account'

    def sign_in_opened(self):
        self.wait_for_element_appear(*self.SIGN_IN_TXT)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_TXT)

    def enter_email(self):
        self.input_text(self.EMAIL, *self.EMAIL_FIELD)

    def enter_password(self):
            self.input_text(self.PASSWORD, *self.PASSWORD_FIELD)

    def click_login(self):
        self.find_element(*self.LOG_IN).click()

    def verify_message(self):
        self.verify_partial_text(self.TEXT,*self.ALERT)