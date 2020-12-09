from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import dep


class BOT:
    def __init__(self, driver_path):
        self.vChrome = webdriver.Chrome(executable_path=driver_path)
        self.group_name = "Dumb Dumb"  # dep.f_group_name()
        self.link = ""

    def url_open(self, link):
        self.vChrome.get(link)


    def nav_to_group(self):
        WebDriverWait(self.vChrome, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
        search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
        self.vChrome.find_element_by_xpath(search_box).click()
        self.vChrome.find_element_by_xpath(search_box).send_keys(self.group_name)

        WebDriverWait(self.vChrome, 20).until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{self.group_name}"]')))
        group_element = self.vChrome.find_element_by_xpath(f'//span[@title="{self.group_name}"]')
        
        group_element.click()


    def nav_to_link(self):
        self.vChrome.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[1]/div/span').click()
        group_search_bar = '//*[@id="app"]/div/div/div[2]/div[3]/span/div/div/div[1]/div/label/div/div[2]'
        self.vChrome.find_element_by_xpath(group_search_bar).click()
        self.vChrome.find_element_by_xpath(group_search_bar).send_keys("https://")
        self.vChrome.find_element_by_xpath(group_search_bar).click()


    def get_link(self):
        message_time_xpath = '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[1]/div[2]'
        WebDriverWait(self.vChrome, 20).until(EC.element_to_be_clickable((By.XPATH, message_time_xpath)))
        time = self.vChrome.find_element_by_xpath(message_time_xpath).text

        #Until You find xpath of the link sleep
        WebDriverWait(self.vChrome, 20).until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/span/span')))

        link_xpath = self.vChrome.find_element_by_xpath(
            '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/span/span')

        while time != dep.get_current_time() or link_xpath.text[0:24] != "https://meet.google.com/":
            time = self.vChrome.find_element_by_xpath(message_time_xpath).text
            link_xpath = self.vChrome.find_element_by_xpath(
                '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/span/span[3]')

        self.link = link_xpath.text
        print(self.link)

