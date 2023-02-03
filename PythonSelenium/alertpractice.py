from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://rahulshettyacademy.com/AutomationPractice/"
name = "Vinod Pawar"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get(url)
driver.maximize_window()
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

## -- Handling Alert pop-up
alertBox = driver.switch_to.alert
alertText = alertBox.text
print(alertText)
assert name in alertText
alertBox.accept()
# alertBox.dismiss()

driver.close()