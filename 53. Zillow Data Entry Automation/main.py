from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from time import sleep

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScDfg2OciF0HzvI_PBW06862GSTiPacTjyJm8dGy5rqNf4oxw/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.84608530611633%2C%22east%22%3A-122.32758609179687%2C%22south%22%3A37.70443074814723%2C%22west%22%3A-122.53907290820312%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"


class DataEntry:
    def __init__(self, driver_path) -> None:
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }

    def get_data(self):
        response = requests.get(ZILLOW_URL, headers=self.headers)
        zillow = response.text

        soup = BeautifulSoup(zillow, "lxml")

        property_prices = soup.find_all("span", {"data-test":"property-card-price"})
        price_list = [price.text for price in property_prices]
        self.price_deals = [cash.split("+")[0] if "+" in cash else cash.split("/")[0] for cash in price_list]

        property_address = soup.find_all("address", {"data-test":"property-card-addr"})
        self.addresses = [address.getText().split(" | ")[-1] for address in property_address]

        self.links = []
        property_links = soup.find_all("a", {"class":"StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0"})
        for link in property_links:
            href = link["href"]
            if "http" not in href:
                self.links.append(f"https://www.zillow.com{href}")
            else:
                self.links.append(href)

    def store_data(self):
        for n in range(len(self.links)):
            try:
                self.driver.get(GOOGLE_FORM_URL)
            except NoSuchElementException:
                self.driver.refresh()
            sleep(5)
            address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

            address.send_keys(self.addresses[n])
            price.send_keys(self.price_deals[n])
            link.send_keys(self.links[n])
            submit_button.click()
            # self.driver.quit()

apartment_deals = DataEntry(CHROME_DRIVER_PATH)
apartment_deals.get_data()
apartment_deals.store_data()
