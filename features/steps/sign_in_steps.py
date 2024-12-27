from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SIGN_IN = (By.ID, 'account-sign-in')

@then('Verify Sign In form opened')
def sign_in_opened(context):
    context.app.sign_in_opened()