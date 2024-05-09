import XLutils
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


s=Service(r"C:\Users\saikr\PycharmProjects\selenium_firstclass\drivers\chromedriver.exe/chromedriver.exe")
driver=webdriver.Chrome(service=s)
#driver = webdriver.Chrome(r"C:\Users\saikr\PycharmProjects\selenium_firstclass\drivers\chromedriver.exe/chromedriver.exe")
url = r"https://igs.imarticus.org/stratonboardportal/uatinternal/"
#url=r"https://practicetestautomation.com/practice-test-login/"
driver.get(url)
driver.maximize_window()
action=ActionChains(driver)
path=r"C:\Users\saikr\Downloads\stratlogindata.xlsx"

rows=XLutils.getRowcount(path,"Sheet1")

driver.find_element(By.XPATH, "//span[@class='select2-selection__arrow']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("Sample Workspace")
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()=' Sample Workspace']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Next']").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//a[@data-wsid='43'])[1]").click()

for r in range(2,rows+1):

    email=XLutils.readData(path,"Sheet1",r,1)
    password=XLutils.readData(path,"Sheet1",r,2)

    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"(//input[@id='signInFormUsername'])[2]").send_keys(email)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"(//input[@id='signInFormPassword'])[2]").send_keys(password)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"(//input[@name='signInSubmitButton'])[2]").click()
    #driver.find_element(By.XPATH,"//input[@name='username']").send_keys(email)
    #driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password)
    #time.sleep(2)
    #driver.find_element(By.XPATH,"//button[@id='submit']").click()


    if driver.title=="Dashboard | Stratonboard":
    #if driver.title == "Logged In Successfully | Practice Test Automation":
        print("passed")
        XLutils.writeData(path,"Sheet1",r,3,"passed")
        action.perform().back()
        driver.find_element(By.XPATH, "(//a[text()='Sign in as a different user?'])[2]").click()
    else:
        print("failed")
        XLutils.writeData(path,"Sheet1",r,3,"failed")

    #driver.find_element(By.XPATH,"//button[@id='page-header-user-dropdown']").click()
    #driver.find_element(By.XPATH,"//span[text()='Sign Out']").click()
    #driver.find_element(By.XPATH,"//button[text()='Submit']").click()
    time.sleep(2)

driver.close()



