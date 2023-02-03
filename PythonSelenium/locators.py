from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

url = "https://rahulshettyacademy.com/angularpractice/"
# -- Service Object creation
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
# -- Webdriver creation for Chrome browser, Invoking webdriver class here
driver = webdriver.Chrome(service=service_obj)
driver.get(url)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".ng-pristine div:nth-child(1) input").send_keys("Vinod Pawar")
driver.find_element(By.NAME, "email").send_keys("demo@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

## -- Select the value from dropdown
# selenium.webdriver.support.select class Select
# Constructor.
# A check is made that the given element is, indeed, a SELECT tag.
# If it is not, then an UnexpectedTagNameException is thrown.
# Example
# from selenium.webdriver.support.ui import Select
# Select(driver.find_element(By.TAG_NAME, "select")).select_by_index(2)

dropDown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropDown.select_by_visible_text("Female")
dropDown.select_by_index(0)
## - Basic Dropdown example finished here


driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Again ")
driver.close()