
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/profile/user-registration")
# driver.find_element_by_xpath("//*[@id='divMain']/div/app-user-registration/div[2]/div/div[2]/div[4]/form/div[5]/div[2]/p-dropdown/div/div[3]/span").click()
ele = driver.find_element(By.TAG_NAME, "span")
drp = Select(ele)
drp.select_by_visible_text("What is your pet name?")