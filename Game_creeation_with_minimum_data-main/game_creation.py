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
# driver = webdriver.Chrome(r"C:\Users\saikr\PycharmProjects\selenium_firstclass\drivers\chromedriver.exe/chromedriver.exe")
url = r"https://igs.imarticus.org/stratonboardportal/uatinternal/"
# url=r"https://practicetestautomation.com/practice-test-login/"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
path = r"C:\Users\saikr\Downloads\gamecreation.xlsx"
rows = XLutils.getRowcount(path, "Sheet1")

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

for r in range(2, rows+1):
    driver.find_element(By.XPATH, "//a[text()=' Create New Game']").click() #clicking create new game button
    time.sleep(2)

    Game_Name= XLutils.readData(path, "Sheet1", r, 2)
    Game_Desc= XLutils.readData(path, "Sheet1", r, 3)
    Per_player_game_validation_days= XLutils.readData(path, "Sheet1", r, 4)
    min_bonous= XLutils.readData(path, "Sheet1", r, 5)
    max_bonous= XLutils.readData(path, "Sheet1", r, 6)
    bd_freq= XLutils.readData(path, "Sheet1", r, 7)
    bd_count= XLutils.readData(path, "Sheet1", r, 8)

    #entering data starts here
    driver.find_element(By.XPATH, "//input[@id='GAME_NAME']").send_keys(Game_Name)
    time.sleep(2)
    driver.find_element(By.XPATH, "//textarea[@id='GAME_DESC']").send_keys(Game_Desc)
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='PER_PLAYER_VALIDITYDAYS']").send_keys(Per_player_game_validation_days)
    time.sleep(2)
    driver.find_element(By.XPATH, "// input[ @ id = 'searchtemplate']").click()
    driver.find_element(By.XPATH, "// a[text() = 'Select Game Template']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='MIN_BONUS']").send_keys(min_bonous)
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='MAX_BONUS']").send_keys(max_bonous)
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='BONUS_FREQUENCY']").send_keys(bd_freq)
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='BONUS_COUNT']").send_keys(bd_count)
    time.sleep(2)

    #Activity unlock mode , it is a dropdown
    activity_unlock_mode = driver.find_element(By.XPATH, "//select[@id='ACTIVITY_UNLOCK_MODE']")
    mode = Select(activity_unlock_mode)
    #mode.select_by_index(2)  # since we are selecting cognito , password textfiled will disappaer
    mode.select_by_visible_text("ALLOPEN")
    time.sleep(2)

    driver.find_element(By.XPATH, "// button[text() = 'Create']").click()
    driver.implicitly_wait(20)

    #alert message will appear , it is a simple alert, whichi is having a OK button.
    driver.find_element(By.XPATH, "// button[text() = 'OK']").click()
    #driver.switch_to.alert.accept() #it is used to click ok button in alert message.
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()='Skip']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()=' Back to Game List']").click()
    time.sleep(2)

driver.close()




