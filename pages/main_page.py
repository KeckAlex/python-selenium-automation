from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    SIGNIN_BTN = (By.ID, 'account-sign-in')
    SIGNIN_BTN_SIDENAV = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')

    def open(self):
        self.open_url('https://www.target.com/')

    def open_cart(self):
        self.open_url('https://www.target.com/cart')

    def click_signin(self):
        self.wait_and_click(*self.SIGNIN_BTN)

    def click_signin_sidenav_btn(self):
        self.wait_and_click(*self.SIGNIN_BTN_SIDENAV)

    def open_sign_in_page(self):
        self.open_url('https://www.target.com/')
        self.wait_and_click(*self.SIGNIN_BTN)
        self.wait_and_click(*self.SIGNIN_BTN_SIDENAV)