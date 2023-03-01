import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--start-maximized")

url = "https://rahulshettyacademy.com/seleniumPractise/#/offers"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH,"//span[contains(text(),'Veg/fruit name')]").click()
nameList = driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
webSortList = []
for names in nameList:
    webSortList.append(names.text)
orignalBrowserSortedList = webSortList.copy()
webSortList.sort()
print(webSortList)
print(orignalBrowserSortedList)
assert orignalBrowserSortedList == webSortList
driver.quit()