import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = "https://rahulshettyacademy.com/seleniumPractise/#/"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
## -- Implict Wait
driver.implicitly_wait(2)
driver.get(url)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
resultCount = len(results)
assert resultCount > 0
for result in results:
    result.find_element(By.XPATH, "div[@class='product-action']/button").click()

# driver.find_element(By.XPATH, "//*[@alt='Cart']").click()                 ## xpath
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()             ##CSS
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

## -- Explicit Wait example
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

actualText = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(actualText)
assert actualText == "Code applied ..!"
totalSum = 0
##-- SUM Validation
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
for price in prices:
    val = int(price.text)
    totalSum = val + totalSum

print(totalSum)
actualTotal = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert totalSum == actualTotal

driver.close()