from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('http://sunland2.test/#/')

robot_elem = driver.find_element_by_id('fixedrobot')
robot_elem.click()

dialog_loc = driver.find_element_by_class_name('dialogRobot')
if dialog_loc.is_displayed():
    left_loc = driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div[2]/div/div[2]/div/section/article[1]/div/div[2]/ul/li')
    left_loc.click()
    time.sleep(2)

    text_loc = driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div[2]/div/div[2]/div/section/article[2]/div[3]/div[1]/textarea')
    text_loc.click()
    text_loc.send_keys('hello world')

    driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div[2]/div/div[2]/div/section/article[2]/div[3]/div[2]/button/span').click()
    time.sleep(5)

    driver.quit()




