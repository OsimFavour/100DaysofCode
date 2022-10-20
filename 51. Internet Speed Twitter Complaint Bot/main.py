from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_EMAIL = os.environ.get('MY_EMAIL2')
TWITTER_PASSWORD = os.environ.get("THE_PASSWORD")
SPEEDTEST_URL = 'https://www.speedtest.net/'
TWITTER_URL = 'https://twitter.com/login'


class InternetSpeedTwitterBot:
    def __init__(self, driver_path) -> None:
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        self.download = 0
        self.upload = 0

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)

        sleep(5)
        accept_cookies = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        accept_cookies.click()

        sleep(5)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        sleep(240)
        self.download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"down: {self.download}")
        print(f"up: {self.upload}")

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)

        # sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        # sign_in_button.click()
        sleep(10)

        login_with_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login_with_username.send_keys(TWITTER_EMAIL)

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        sleep(5)
        password.send_keys(Keys.ENTER)

        sleep(10)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.download}down/{self.upload}up"
            f" when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up")

        sleep(10)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        sleep(2)
        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
