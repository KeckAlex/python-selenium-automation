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