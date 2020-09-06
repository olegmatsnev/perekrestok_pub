#!/usr/bin/python
import keyring
from selenium import webdriver
import time
import datetime
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--silent')
options.add_argument('log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chromedriver_path = 'D:\ARCHIVE\Meteo\Logs\chromedriver.exe'
driver = webdriver.Chrome(chromedriver_path, options=options)

driver.get('https://www.perekrestok.ru/')
driver.find_element_by_xpath("//div[@class='xfnew-header__user-nav js-auth-modal-opener']").click()
login = driver.find_element_by_xpath("//input[@id='login-popup-login']")
login.send_keys("email@address")
pwd = driver.find_element_by_xpath("//input[@id='login-popup-password']")
pwd.send_keys(keyring.get_password('perekrestok', 'email@address'))
driver.find_element_by_xpath("//button[@id='button-submit-login']").click()
time.sleep(1)
delivery_date = driver.find_element_by_xpath("//span[@class='xfnew-slot-informer__date']").text
if delivery_date != '':
    print('Ближайшая доставка', delivery_date)
else:
    print('Свободных интервалов доставки нет')
