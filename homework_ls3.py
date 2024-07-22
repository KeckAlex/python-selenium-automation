from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 1. ################################################################

# open the url
driver.get('https://www.amazon.com/')

# find and open "create new account" link
driver.find_element(By.CSS_SELECTOR, "#nav-flyout-ya-newCust a").click()

# find "amazon" logo
driver.find_element(By.CSS_SELECTOR, "#a-page .a-icon-logo")

# find "create account" element
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# find "your name" field
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# find "email" field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# find "password" field
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# find "Passwords must be at least 6 characters" note
driver.find_element(By.XPATH, "//div[@class='a-alert-content' and contains(text(),'6 characters.')]")

# find "Re-enter password" field
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# find "Continue"/"Create your Amazon account" button
driver.find_element(By.CSS_SELECTOR, "#continue")

# find "Conditions of Use" link
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

# find "Privacy Notice" link
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice']")

# find "Sign in" link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

# 2.#######################################################################

# open the URL
driver.get('https://www.target.com/')
# find the cart and click on it
driver.find_element(By.CSS_SELECTOR, "use[href='/icons/Cart.svg#Cart']").click()
sleep(3)
# verify "Your cart is empty" message is shown
expected_text = 'Your cart is empty'
actual_text = driver.find_element(By.CSS_SELECTOR, "#cart-container h1").text
print(actual_text)
assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}'

print('Test case passed')
driver.quit()

# 3.#########################################################################

# open the URL
driver.get('https://www.target.com/')
# click Sign In
driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()
sleep(3)
# from right side navigation menu, click Sign In
driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
sleep(3)
# verify Sign In form is opened
expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.CSS_SELECTOR, "#__next h1").text
print(actual_text)
assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}'

print('Test case passed')
driver.quit()