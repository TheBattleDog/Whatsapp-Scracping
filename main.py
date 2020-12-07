from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date
import Functions

vChrome = webdriver.Chrome(executable_path="C:/Users/AK/Documents/Code/Whatsapp/chromedriver.exe")
vChrome.get("https://web.whatsapp.com")

time.sleep(10)

GropName = Functions.group_nav()

vChrome.find_element_by_xpath(f'//span[@title="{GropName}"').click()