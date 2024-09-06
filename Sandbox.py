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