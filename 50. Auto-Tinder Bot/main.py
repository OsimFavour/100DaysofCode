"""
In Selenium, each window has an identification handle, we can get all the window handles with:
driver.window_handles

The above line of code returns a list of all the window handles. The first window is at position 0 e.g.
base_window = driver.window_handles[0]

New windows that have popped out from the base_window are further down in the sequence e.g.
fb_login_window = driver.window_handles[1]

We can switch our Selenium to target the new facebook login window by:
driver.switch_to.window(fb_login_window)

You can print the driver.title to verify that it's the facebook login window that is currently target:
print(driver.title)
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path, options=options)

URL = 'https://tinder.com/'
EMAIL = "osimfavour000@gmail.com"
PASSWORD = "Mmumene02"
TINDER_CODE = "199877"

driver.get(URL)

sleep(10)
decline_cookies = driver.find_element(By.XPATH, '//*[@id="q1623655810"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
decline_cookies.click()

sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="q1623655810"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()
sleep(5)

login_with_facebook = driver.find_element(By.XPATH, '//*[@id="q-104725266"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
login_with_facebook.click()
sleep(7)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(f"We just switched to {driver.title} window...")

email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(EMAIL)

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(PASSWORD)
sleep(2)
submit_details = password.send_keys(Keys.ENTER)

# sleep(5)
# login_verification = driver.find_element(By.XPATH, '//*[@id="approvals_code"]')
# login_verification.send_keys(TINDER_CODE)
# login_verification.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(f"We are back to {driver.title}")

try:
    sleep(10)
    allow_button = driver.find_element(By.XPATH, '//*[@id="q-104725266"]/main/div/div/div/div[3]/button[1]/span')
    allow_button.click()
except NoSuchElementException:
    sleep(20)

sleep(5)
not_interested_button = driver.find_element(By.XPATH, '//*[@id="q-104725266"]/main/div/div/div/div[3]/button[2]/span')
not_interested_button.click()


for n in range(100):
    sleep(5)
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="q1623655810"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span/svg')
        like_button.click()
        print(f"Like number {n}")
    except ElementClickInterceptedException:
        print("It's a Match")
        match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
        match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
    except NoSuchElementException:
        sleep(5)
        
    
# driver.quit()
