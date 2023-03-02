from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

## ----------------------------------------  ##
chrome_options = webdriver.ChromeOptions()                  ##-- Created chrome option to run in headless mode
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--safebrowsing-disable-extension-blacklist")
chrome_options.add_argument("--safebrowsing-enable")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--safebrowsing-disable-download-protection")
chrome_options.add_argument("--start-maximized")
## ----------------------------------------  ##
url = "https://rahulshettyacademy.com/angularpractice/"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)
driver.get(url)
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
productList = driver.find_elements(By.XPATH,"//*[@class='card h-100']")
for product in productList:
    prodName = product.find_element(By.XPATH,"div/h4/a").text
    if prodName == "Nokia Edge":
        product.find_element(By.XPATH, "div/button").click()
        break
driver.find_element(By.XPATH,"//li[@class='nav-item active']/a").click()
driver.find_element(By.CSS_SELECTOR,"button[class*='btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox']").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[contains(text(),'India')]")))
driver.find_element(By.XPATH, "//a[contains(text(),'India')]").click()
driver.find_element(By.CSS_SELECTOR, "input[class*='btn-success']").click()
succMess = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
assert "Success! Thank you!" in succMess
driver.quit()