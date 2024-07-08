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

# open the url
driver.get('https://www.amazon.com/')

# Amazon logo
driver.find_element(By.ID, "//a[@id='nav-logo-sprites']")
driver.find_element(By.XPATH, "//a[@class='nav-logo-link nav-progressive-attribute']")

# find and open login link
driver.find_element(By.XPATH, "//a[@data-nav-ref='nav_ya_signin']").click()
driver.find_element(By.ID, "//a[@id='nav-link-accountList']").click()
driver.find_element(By.XPATH, "//span[@class='nav-action-inner']").click()

# Email field
driver.find_element(By.XPATH, "//input[@aria-describedby='Enter your email or mobile phone number']")

# Continue button
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

# Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'condition_of_use')]") #by parent

# Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, "//a[@id='auth-fpp-link-bottom']")

# Other issues with Sign-in link
driver.find_element(By.ID, "//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
driver.find_element(By.ID, "//a[@id='createAccountSubmit']")

# Open https://www.target.com/
driver.get('https://www.target.com/')
# find and click SignIn button
driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()
# click SignIn from side navigation
driver.find_element(By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy' and text()='Sign in']").click()
sleep(5)
# verify SignIn page opened
# expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text
print(actual_text)
# assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}'
sleep(5)
# print('Test case passed')
driver.quit()