from datetime import date
import math
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BOT:
    def __init__(self, driver_path):
        self.vChrome = webdriver.Chrome(executable_path=driver_path)
        self.group_name = f_group_name()
        self.


def DayFinder(todays_date):
    sDate = str(todays_date)
    day = int(sDate[-1]) if sDate[-2] == '0' else int(sDate[-2:len(sDate)])
    month = int(sDate[6]) if sDate[5] == '0' else int(sDate[5:7])
    year = int(sDate[0:4])
    if month < 3:
        year -= 1
        day += year
        day_name = day
    else:
        day += year - 2
        day_name = day
    day_name = math.floor(int(23 * month / 9 + day + 4 + year / 4 - year / 100 + year / 400) % 7)
    if day_name == 0:    return "Sunday"
    if day_name == 1:    return "Monday"
    if day_name == 2:    return "Tuesday"
    if day_name == 3:    return "Wednesday"
    if day_name == 4:    return "Thursday"
    if day_name == 5:    return "Friday"
    if day_name == 6:    return "Saturday"


def f_group_name():
    Today = DayFinder(date.today())
    now = datetime.now()
    sub1 = now.replace(hour=9, minute=30, second=0, microsecond=0)
    management = "S1 Bcom CA Carmel"
    methodology = "S1 B Com CA(methodology )"
    iit = "S1 B.Com CA (I I T )"
    english = "S1 CA English"
    economics = "Managerial Economics C A"
    evs = "S1 B.Com C A (EVS )"
    if Today == "Monday":
        if now < sub1:
            return management
        else:
            return evs
    elif Today == "Tuesday":
        if now < sub1:
            return methodology
        else:
            return iit
    elif Today == "Wednesday":
        if now < sub1:
            return english
        else:
            return management
    elif Today == "Thursday":
        if now < sub1:
            return iit
        else:
            return economics
    elif Today == "Friday":
        if now < sub1:
            return evs
        else:
            return english
    else:
        while True:
            subject = input("Enter the subject >> ")
            subject = subject.lower()
            if subject == "management":
                return management
            if subject == "EVS":
                return evs
            if subject == "meth" or subject == "methodology":
                return methodology
            if subject == "iit":
                return iit
            if subject == "eng" or subject == "english":
                return english
            if subject == "economics" or subject == "managerial economics" or subject == "eco":
                return economics
            else:
                print("Invalid Input please try again\n Valid Input = Management, EVS, Meth, IIT and ENG.")

def group_nav(vChrome, GroupName):
    SearchBox = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    vChrome.find_element_by_xpath(SearchBox).click()
    vChrome.find_element_by_xpath(SearchBox).send_keys(GroupName)

    WebDriverWait(vChrome, 20).until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{GroupName}"]')))
    GroupElement = vChrome.find_element_by_xpath(f'//span[@title="{GroupName}"]')

    GroupElement.click()