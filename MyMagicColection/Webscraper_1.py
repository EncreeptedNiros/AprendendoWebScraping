import time
from selenium.webdriver.common.by import By
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import json

url = 'https://scryfall.com/search?as=grid&order=name&q=type%3Avampire+%28game%3Apaper%29'

option = Options()
option.headless = True
driver = webdriver.Firefox()
flag = 0
driver.get(url)
time.sleep(10)
for j in range(7):
    for i  in range(60):
        try:
            paths = "//html//body//div[3]//div[3]//div//div["+ str(i+1) +"]//a//div//div//img"
            print(driver.find_element(By.XPATH, paths).get_attribute('title') + "\n")
        except Exception:
            print("no card")
    if (flag == 0):
        driver.find_element(By.XPATH, "//html//body//div[3]//div[1]//div//div[2]//a[1]").click()
        flag = 1
    else:
        try:
            driver.find_element(By.XPATH, "//html//body//div[3]//div[1]//div//div[2]//a[3]").click()
        except Exception:
            print("no page")
    time.sleep(10)


driver.quit()