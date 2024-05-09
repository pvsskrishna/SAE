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

print("Dashboard id displayed")

# clicking on "View More" button in Leaderboard panel in Dashboard UI
driver.find_element(By.XPATH, "//a[text()='View More']").click()
time.sleep(10)
print("Detailed Leaderboard is displayed")

# driver.find_element(By.XPATH, "//a[@title='Download']").click()
driver.get(r"https://igs.imarticus.org/stratonboardportal/uatinternal/Portal/exportdetailedLeaderboard/43/34")
'''the above mentioned url is the url of the downloader button, if we open that link in new tab file will get download 
automatically '''
time.sleep(10)
print("file was downloaded")
driver.close()
