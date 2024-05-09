import self as self

import XLutils
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

s = Service(r"C:\Users\saikr\PycharmProjects\selenium_firstclass\drivers\chromedriver.exe/chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = r"https://igs.imarticus.org/stratonboardportal/uatinternal/"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

# workspace selection UI
driver.find_element(By.XPATH, "//span[@class='select2-selection__arrow']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("Sample Workspace")  # entered workspace name
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()=' Sample Workspace']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Next']").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//a[@id='fedlogin'])[1]").click()
time.sleep(2)

# login UI
driver.find_element(By.XPATH, "(//input[@id='signInFormUsername'])[2]").send_keys("varun.paladugula@imarticus.com")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "(//input[@id='signInFormPassword'])[2]").send_keys('Password@22')
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "(//input[@name='signInSubmitButton'])[2]").click()
driver.implicitly_wait(5)

# entered into Authoring Engine
# now configuring the game
driver.find_element(By.XPATH, "//span[text()='Configurations']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//p[text()='Game Configuration']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Manage Game']").click()
time.sleep(2)

# clicking on statistics button, on our desired game
element = driver.find_element(By.XPATH, "(//a[@title='Statistics'])[44]")
driver.execute_script("arguments[0].click();", element)
time.sleep(10)

# clicking close on popup
driver.find_element(By.XPATH, "(//button[text()='Close'])[1]").click()
time.sleep(2)

# again clicking on statistics button, on our desired game
element = driver.find_element(By.XPATH, "(//a[@title='Statistics'])[44]")
driver.execute_script("arguments[0].click();", element)
time.sleep(2)

# clicking on download button
driver.find_element(By.XPATH, "//a[@id='downloadstatbtn']").click()
time.sleep(2)

# clicking on cross button/ closing the popup
driver.find_element(By.XPATH, "//button[@class='close']").click()
time.sleep(2)

driver.close()


