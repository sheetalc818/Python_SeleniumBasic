import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(2)
driver.save_screenshot("/home/sheetal/PycharmProjects/Selenium_Basics/Resources/Screenshot/firstscreenshot.png")
