from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://rahulshettyacademy.com/AutomationPractice/"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get(url)
driver.maximize_window()
checkBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# print(len(checkBoxes))
for checkbox in checkBoxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

# radioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")   ## - with xpath
radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")               ## -- With css selector class name
for radiobutton in radioButtons:
    if radiobutton.get_attribute("value") == "radio3":
        radiobutton.click()
        assert radiobutton.is_selected()


assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
driver.close()