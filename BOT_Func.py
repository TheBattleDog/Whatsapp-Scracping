from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
import dep
from os import system
from time import sleep


class BOT:
    def __init__(self, driver_path):
        self.vChrome = webdriver.Chrome(executable_path=driver_path)
        self.group_name = "Dumb Dumb"  # "S1 Bcom CA Carmel"  # change gruop_name to self.f_group_name()
        self.link = ""
        self.group_search_bar = '//*[@id="app"]/div/div/div[2]/div[3]/span/div/div/div[1]/div/label/div/div[2]'
        self.group_num = 0

    def wait_until(self, xpath, time=20):
        WebDriverWait(self.vChrome, time).until(EC.element_to_be_clickable((By.XPATH, xpath)))


    def url_open(self, link):
        self.vChrome.get(link)

    def f_group_name(self):
        if self.group_num == 1:
            self.group_name = "S1 Bcom CA Carmel"
        elif self.group_num == 2:
            self.group_name = "S1 B Com CA(methodology )"
        elif self.group_num == 3:
            self.group_name = "S1 B.Com CA (I I T )"
        elif self.group_num == 4:
            self.group_name = "S1 CA English"
        elif self.group_num == 5:
            self.group_name = "Managerial Economics C A"
        elif self.group_num == 6: 
            self.group_name = "S1 B.Com C A (EVS )"
        else:
            self.group_num = 1
            self.group_name = "S1 Bcom CA Carmel"


    def nav_to_group(self):
        WebDriverWait(self.vChrome, 20).until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
        search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
        self.vChrome.find_element_by_xpath(search_box).click()
        self.clear_text_area(search_box)
        self.vChrome.find_element_by_xpath(search_box).send_keys(self.group_name)

        WebDriverWait(self.vChrome, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="matched-text _1VzZY"]')))
        group_element = self.vChrome.find_element_by_xpath('//span[@class="matched-text _1VzZY"]')
        clicked = ""
        while clicked == "":
            try:
                sleep(1)
                clicked = group_element.click()
            except ElementClickInterceptedException:
                continue


    def nav_to_link(self):
        self.wait_until('//*[@id="main"]/header/div[3]/div/div[1]/div/span', 20)
        sleep(1)
        self.vChrome.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[1]/div/span').click()
        self.vChrome.find_element_by_xpath(self.group_search_bar).click()
        self.vChrome.find_element_by_xpath(self.group_search_bar).send_keys("https://meet.google.com/")


    def clear_text_area(self, xpath_to_clear):
        area = self.vChrome.find_element_by_xpath(xpath_to_clear)
        # Clear the Search field by pressing Ctrl + Backspace (Ctrl = u'\ue009' Backspace = u'\ue003')
        while len(area.text):
            area.send_keys(u'\ue009' + u'\ue003')


    def get_link(self):

        while True:
            message_time_xpath = '//div[@class="_2gsiG"]'
            WebDriverWait(self.vChrome, 100000).until(EC.element_to_be_clickable((By.XPATH, message_time_xpath)))
            time = dep.to_time(self.vChrome.find_element_by_xpath(message_time_xpath).text)

            #Until You find xpath of the link sleep
            WebDriverWait(self.vChrome, 20).until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/span/span')))

            link_xpath = self.vChrome.find_element_by_xpath(
                '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/span/span')

            WebDriverWait(self.vChrome, 20).until(EC.element_to_be_clickable((
                By.XPATH, '//span[@class="_1hI5g _1XH7x _1VzZY"][@dir="ltr"]')))


            self.wait_until(self.group_search_bar, 20)
            self.clear_text_area(self.group_search_bar)
            self.vChrome.find_element_by_xpath(self.group_search_bar).send_keys("https://meet.google.com/")
            try:
                WebDriverWait(self.vChrome, 20).until(EC.presence_of_element_located((
                    By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/span/span')))
                if time.hour == dep.get_current_time().hour and link_xpath.text[0:24] == "https://meet.google.com/":
                    break
                else:
                    self.clear_text_area(self.group_search_bar)
                    self.group_num += 1
                    self.f_group_name()
                    self.nav_to_group()
                    self.nav_to_link()
            except StaleElementReferenceException:
                sleep(1)
                if time.hour == dep.get_current_time().hour and link_xpath.text[0:24] == "https://meet.google.com/":
                    break
                else:
                    self.clear_text_area(self.group_search_bar)
                    self.group_num += 1
                    self.f_group_name()
                    self.nav_to_group()
                    self.nav_to_link()

        self.link = link_xpath.text


    def write_link_file(self):
        html_code = f'''<html>
<head>
    <script>
        window.location.href = "{self.link}"
    </script>
</head>
</html>'''
        file = open("link.html", "w")
        file.write(html_code)
        file.close()


    def invoke_js_file(self):
        system("start link.html")
