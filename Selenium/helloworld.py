from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)

capabilities = {
    "build" : os.getenv("LT_BUILD_NAME"),
    "name" : "BAH HW Test",
    "platform" : "Windows 10",
    "browserName" : "Chrome",
    "version" : "88.0",
    "resolution" : "1920x1080",
    "tunnel" : True
}

driver.get("http://192.168.1.149:8081/")
assert "No results found." not in driver.page_source
print("Selenium Test Started")
print("Page Title from source code: " + driver.title)
driver.save_screenshot('s1.png')
screenshot = Image.open('s1.png')
#screenshot.show() #commented for CLI run-time
assert "Selenium Test" in driver.title
driver.find_element("id", "pipe").click()
assert "http://192.168.1.149:8081/pipeline.html" in driver.current_url
driver.save_screenshot('s2.png')
screenshot2 = Image.open('s2.png')
#screenshot2.show() #commented for CLI run-time
assert "Version" in driver.page_source
version = driver.find_element("id", "version").text
driver
print("Current Version Info: " + version)
print("Selenium Test Complete - Test Pass")
driver.quit()