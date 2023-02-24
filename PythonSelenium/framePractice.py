from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/iframe"
service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get(url)
driver.maximize_window()
iframe = driver.find_element(By.XPATH,"//iframe[@title='Rich Text Area']")
driver.switch_to.frame(iframe)
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("An inline frame (iframe) is a HTML element that loads another HTML page within the document. An iframe is used in webpages where external content is displayed like vidoes, advertisements, Google Maps, etc.")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
driver.quit()