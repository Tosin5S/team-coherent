#!/bin/env python3
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from urllib.parse import urlparse, parse_qs
from selenium.webdriver.chrome.options import Options

class FacebookCrawl():
    """Get information about a user on a social media"""
    facebook_id = None
    def __init__(self, link) -> None:
        """Initialize SocialSearcher"""
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--window-size=1920,1080')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')

        current_script_path = os.path.abspath(__file__)
        current_dir_path = os.path.dirname(current_script_path)
        filename = "chrome/opt/google/chrome/google-chrome"
        file_path = os.path.join(current_dir_path, filename)
        driver_path = os.path.join(current_dir_path, 'chromedriver')
        chrome_options.binary_location = file_path
        print("init")
        self.driver = webdriver.Chrome(
            executable_path=driver_path, options=chrome_options)
        print("get link")
        self.driver.get("https://commentpicker.com/find-facebook-id.php")
        print("waiting")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "js-facebook-link")))
        self.profile_url = link
        print(f"{link} gotten")

    def get_user_id(self):
        """Get the id of the facebook user"""

        profile_input = self.driver.find_element(By.ID, "js-facebook-link")
        profile_input.send_keys(self.profile_url)
        captcha_x = self.driver.find_element(By.ID, "captcha-x")
        captcha_y = self.driver.find_element(By.ID, "captcha-y")
        captcha = f"{captcha_x.text} + {captcha_y.text}"
        result = eval(captcha)
        self.driver.find_element(By.ID, "captcha").send_keys(result)
        self.driver.find_element(By.ID, "js-start-button").click()



crawl = FacebookCrawl("https://web.facebook.com/adebisi.bukola.372")
print(crawl.get_user_id())