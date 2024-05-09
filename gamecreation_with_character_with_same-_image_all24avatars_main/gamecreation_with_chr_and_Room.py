#chr=character, without room
import self as self
#used same image for all the character creations
import XLutils
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

s = Service(r"C:\Users\saikr\PycharmProjects\selenium_firstclass\drivers\chromedriver.exe/chromedriver.exe")

#s = Service(r"C:\Users\saikr\PycharmProjects\selenium_firstclass\drivers\geckodriver.exe")
driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome(r"C:\Users\saikr\PycharmProjects\selenium_firstclass\drivers\chromedriver.exe/chromedriver.exe")
url = r"https://igs.imarticus.org/stratonboardportal/uatinternal/"
# url=r"https://practicetestautomation.com/practice-test-login/"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
path = r"C:\Users\saikr\Downloads\character_creation.xlsx"
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
driver.implicitly_wait(5)
print("before clicking 44th element")


element=driver.find_element(By.XPATH, "(//i[@class='fas fa-user-plus'])[44]")
driver.execute_script("arguments[0].click();", element)

# character_create=driver.find_element(By.XPATH, "(//a[@title='Character create'])[44]")
# actions=ActionChains(driver)
# actions.move_to_element(character_create)
# actions.perform()
print("action 3d")
driver.implicitly_wait(5)



for r in range(2, rows+1):
    chr_Name= XLutils.readData(path, "Sheet1", r, 2)
    chr_Desig= XLutils.readData(path, "Sheet1", r, 3)
    chr_role= XLutils.readData(path, "Sheet1", r, 4)

    driver.find_element(By.XPATH, "//a[text()=' Add Character']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='avatar_name']").send_keys(chr_Name)
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='avatar_designation']").send_keys(chr_Desig)
    time.sleep(2)
    driver.find_element(By.XPATH, "(//button[text()='Browse'])[1]").click()
    time.sleep(2)

    if r == 2:#avatar id='39'
        driver.find_element(By.XPATH, "//div[@id='39']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 3:
        driver.find_element(By.XPATH, "//div[@id='41']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 4:
        driver.find_element(By.XPATH, "//div[@id='42']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 5:
        driver.find_element(By.XPATH, "//div[@id='43']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 6:
        driver.find_element(By.XPATH, "//div[@id='44']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 7:
        driver.find_element(By.XPATH, "//div[@id='45']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 8:
        driver.find_element(By.XPATH, "//div[@id='46']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 9:
        driver.find_element(By.XPATH, "//div[@id='47']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 10:
        driver.find_element(By.XPATH, "//div[@id='48']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 11:
        driver.find_element(By.XPATH, "//div[@id='49']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 12:
        driver.find_element(By.XPATH, "//div[@id='50']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 13:
        driver.find_element(By.XPATH, "//div[@id='51']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 14:
        driver.find_element(By.XPATH, "//div[@id='52']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 15:
        driver.find_element(By.XPATH, "//div[@id='53']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 16:
        driver.find_element(By.XPATH, "//div[@id='54']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 17:
        driver.find_element(By.XPATH, "//div[@id='55']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 18:
        driver.find_element(By.XPATH, "//div[@id='56']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 19:
        driver.find_element(By.XPATH, "//div[@id='57']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 20:
        driver.find_element(By.XPATH, "//div[@id='58']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 21:
        driver.find_element(By.XPATH, "//div[@id='59']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 22:
        driver.find_element(By.XPATH, "//div[@id='60']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 23:
        driver.find_element(By.XPATH, "//div[@id='61']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 24:
        driver.find_element(By.XPATH, "//div[@id='62']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()
    if r == 25:
        driver.find_element(By.XPATH, "//div[@id='63']").click()
        driver.find_element(By.XPATH, "(//button[text()='Select'])[1]").click()

    driver.find_element(By.XPATH, "//input[@id='avatar_role']").send_keys(chr_role)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Next']").click()
    time.sleep(2)

    #content adding ui
    driver.find_element(By.XPATH, "//a[@class='togglesidebar']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@id='addimage']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "// button[ @ id = 'pills-browse-tab']").click()
    time.sleep(2)
    choose_image=driver.find_element(By.XPATH, "// input[ @ id = 'imageuploadbrowse']")
    choose_image.send_keys(r"C:\Users\saikr\Pictures\Screenshots\choose_image.png") #uplodiing image
    time.sleep(2)

    # if the image is already exist, clicking on continue in the popup
    if driver.find_element(By.XPATH, "//button[text() = 'Continue']").is_displayed():
        driver.find_element(By.XPATH, "//button[text() = 'Continue']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@id='addImgsubmitBtn']").click()
    driver.implicitly_wait(10)

    #driver.find_element(By.XPATH, "(// button[text() = 'Apply'])[2]").click()
    save=driver.find_element(By.XPATH, "//button[text()='Save']")
    driver.execute_script("arguments[0].click();", save)
    time.sleep(2)
driver.close()

