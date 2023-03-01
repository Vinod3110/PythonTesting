from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "https://rahulshettyacademy.com/AutomationPractice/"
chrome_options = webdriver.ChromeOptions()                  ##-- Created chrome option to run in headless mode
# chrome_options.add_argument("headless")                     ##-- for running script in headless mode

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

service_obj = Service("C:/Users/VINOD/Webdrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)
driver.get(url)
# driver.maximize_window()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")  ## -- for executing the Java script through selenium
# driver.get_screenshot_as_file("screenshot.png")   ## -- To Take the screenshots

driver.quit()