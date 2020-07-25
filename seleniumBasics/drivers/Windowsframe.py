import time

from selenium import  webdriver
from  selenium.webdriver import  ActionChains

driver =webdriver.Chrome("D:\\chromedriver_win32 (5)\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/windows.html")
driver.maximize_window()
ele1 = driver.find_element_by_xpath("//a[text()= 'SwitchTo']")
ele2 = driver.find_element_by_xpath("//a[text()='Windows']")
ActionChains(driver).move_to_element(ele1).move_to_element(ele2).click().perform()
time.sleep(5)
driver.find_element_by_xpath("//a[text()='Open New Seperate Windows']").click()
driver.find_element_by_xpath("//button[text()= ''").click()

windowsize=driver.window_handles
print(windowsize)
for handle in windowsize:
    driver.switch_to_window(handle)
time.sleep(5)


#driver.find_element_by_xpath("//a[text()=''])[2].click()
#driver.find_element_by_xpath("//input[@placeholder='')").send_keys(kartik)
