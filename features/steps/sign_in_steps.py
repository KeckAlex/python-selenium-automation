from selenium.webdriver.common.by import By
from behave import given, when, then


SIGN_IN = (By.ID, 'account-sign-in')

@then('Verify Sign In form opened')
def sign_in_opened(context):
    context.app.sign_in_page.sign_in_opened()

@then('Enter email address')
def enter_email(context):
    context.app.sign_in_page.enter_email()

@then('Enter password')
def enter_password(context):
    context.app.sign_in_page.enter_password()

@then('Click login button')
def click_login(context):
    context.app.sign_in_page.click_login()

@then('Verify “We cannot find your account.” message is shown')
def verify_message(context):
    context.app.sign_in_page.verify_message()