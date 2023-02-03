from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://rahulshettyacademy.com/client/"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get(url)
driver.maximize_window()
# driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
## -- Xpath creation with text present on the web page
# driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
## -- Xpath creation with text contains  on the web page
# driver.find_element(By.XPATH, "//button[contains(text(),'Save New Password')]").click()

driver.close()
