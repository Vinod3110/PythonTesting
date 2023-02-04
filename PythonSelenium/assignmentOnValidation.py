import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []
url = "https://rahulshettyacademy.com/seleniumPractise/#/"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)                   ##--Implicit wait for project
driver.get(url)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys('Ber')
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
resultCount = len(results)
assert resultCount > 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div[@class='product-action']/button").click()
print(actualList)
assert expectList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
##-- Explict Wait Starts here
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
##-- Explict Wait Ends here

totalAmount = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
amountAfterDisc = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(totalAmount)
print(amountAfterDisc)
assert totalAmount > amountAfterDisc
driver.close()