from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


service = Service("/Users/kumail/Documents/Development/chromedriver")
SIMILAR_ACCOUNT = "foodnetwork"
USERNAME = "kazmm4910"
PASSWORD = "abcd123abcd"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        username_field = self.driver.find_element(By.NAME, 'username')
        username_field.send_keys(f'{USERNAME}')
        username_field.send_keys(Keys.TAB)
        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(f'{PASSWORD}')
        log_in_button = self.driver.find_element(By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF')
        log_in_button.click()
        time.sleep(10)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)
        follower_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        follower_button.click()
        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for button in follow_buttons:
            if button.text != "Follow":
                pass
            else:
                button.click()
                time.sleep(2)


bot = InstaFollower(service)
bot.login()
bot.find_followers()
bot.follow()
