from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/windows"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)                   ##--Implicit wait for project
driver.get(url)
driver.maximize_window()


driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles
# print(windowsOpened)
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.XPATH,"//div[@class='example']/h3").text)
driver.close()
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,'h3').text
print(driver.find_element(By.TAG_NAME,'h3').text)
# driver.close()
driver.quit()