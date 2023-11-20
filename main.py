from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from account_credentials import username,password
from targetted_account import target_acc

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.instagram.com/")

driver.implicitly_wait(5)


input_username = driver.find_element(By.NAME,'username')
input_username.send_keys(username)
input_password = driver.find_element(By.NAME,'password')
input_password.send_keys(password)
login_button = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')
login_button.click()

driver.get(f"https://www.instagram.com/{target_acc}")


