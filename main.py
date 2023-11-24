from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from account_credentials import username, password
from targetted_account import target_acc
from time import sleep as time_sleep

class FollowerBot:

    def __init__(self,username,password, target_acc):

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.username = username
        self.password = password
        self.target_acc = target_acc

    def instagram(self):
        self.driver.get("https://www.instagram.com/")

    def login(self):
        # Wait for the username input field to be present
        input_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        input_username.send_keys(self.username)

        # Wait for the password input field to be present
        input_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        input_password.send_keys(self.password)
        click_login = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
        click_login.click()

    def target_account(self):
        self.driver.get(f"https://www.instagram.com/{self.target_acc}")

    def follow_accounts(self):
        follower_count_button=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower_count_button.click()


d = FollowerBot("businessgenerate","Allah78666","businessdrivendream")
d.instagram()
d.login()
WebDriverWait(d.driver, 10).until(EC.url_changes("https://www.instagram.com/"))
d.target_account()
WebDriverWait(d.driver, 10).until(EC.url_changes("https://www.instagram.com/"))
d.follow_accounts()

