from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = "https://rahulshettyacademy.com/loginpagePractise/"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get(url)
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
openedWindows = driver.window_handles
print(openedWindows)
driver.switch_to.window(openedWindows[1])
userName = driver.find_element(By.XPATH,"//div/p[2]/strong/a").text
# print(userName)
driver.switch_to.window(openedWindows[0])
driver.find_element(By.CSS_SELECTOR,"[id='username']").send_keys(userName)
driver.find_element(By.ID,"password").send_keys("Pass12345")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
errorMessage = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
# assert "Incorrect" == errorMessage
print(errorMessage)
# driver.close()
driver.quit()