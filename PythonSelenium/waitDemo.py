from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://rahulshettyacademy.com/seleniumPractise/#/"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get(url)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".search-button").send_keys("ber")
