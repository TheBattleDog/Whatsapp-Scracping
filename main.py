from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from datetime import date
import Functions

vChrome = webdriver.Chrome(executable_path="C:/Users/AK/Documents/Code/Whatsapp/chromedriver.exe")
vChrome.get("https://web.whatsapp.com")

GroupName = Functions.group_nav()

WebDriverWait(vChrome, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div')))

SearchBox = vChrome.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div')
SearchBox.click()
vChrome.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(GroupName)

WebDriverWait(vChrome, 20).until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{GroupName}"]')))
GroupElement = vChrome.find_element_by_xpath(f'//span[@title="{GroupName}"]')

GroupElement.click()
