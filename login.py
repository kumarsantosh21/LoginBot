from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import schedule
import time

global c1
c1 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]'
global c2
c2 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]/div/div[2]'
global c3
c3 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]'
global c4
c4 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[4]/div/div[2]'
global c5
c5 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[4]/div/div[2]'


def onehour(arg1):

    driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
    driver.get('https://myclass.lpu.in/')
    driver.maximize_window()

    id = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
    id.send_keys("Reg Id")

    password= driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys("Password")

    logi = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()

    window1 = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a').click()


    time.sleep(10)



    class3rd =driver.find_element_by_xpath(arg1)
    class3rd.click()
 
    time.sleep(10)

    joinB = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(15)

    act = ActionChains(driver)

    for i in range(3):
        act.send_keys(Keys.TAB).perform()



    act.send_keys(Keys.ENTER).perform()
    time.sleep(3300)
    driver.close()


def twohour(arg2):

    driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
    driver.get('https://myclass.lpu.in/')
    driver.maximize_window()

    id = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
    id.send_keys("Reg Id")

    password= driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys("Password")

    logi = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()

    window1 = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a').click()


    time.sleep(10)



    class3rd =driver.find_element_by_xpath(arg2)
    class3rd.click()
 
    time.sleep(10)

    joinB = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(15)

    act = ActionChains(driver)

    for i in range(3):
        act.send_keys(Keys.TAB).perform()



    act.send_keys(Keys.ENTER).perform()


    time.sleep(6900)
    driver.close()

def rest():
    quit()

def timer():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"The Time is: {current_time}")
   
schedule.every(60).seconds.do(timer)


schedule.every().monday.at("09:05").do(twohour, c1)

schedule.every().tuesday.at("11:03").do(onehour, c1)

schedule.every().saturday.at("14:26").do(onehour, c1)





schedule.every().saturday.at("18:30").do(rest)

while True:
    schedule.run_pending()
    time.sleep(1)
