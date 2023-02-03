from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "https://rahulshettyacademy.com/"
url1 = "https://rahulshettyacademy.com/seleniumPractise/#/"
url2 = "https://courses.rahulshettyacademy.com/courses"
url3 = "https://rahulshettyacademy.com/loginpagePractise/"

## Chrome Browser Object Creation
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

## Firefox Browser Object Creation
# service_obj = Service("C:/Users/VINOD/Webdrivers/geckodriver-v0.32.0-win32/geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

## Edge Browser Object Creation
# sevice_obj = Service("C:/Users/VINOD/Webdrivers/edgedriver_win64/msedgedriver.exe")
# driver = webdriver.Edge(service=sevice_obj)

### Actual Selenium Work starts

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
if url == driver.current_url:
    print("User on right URL")
driver.get(url1)
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()