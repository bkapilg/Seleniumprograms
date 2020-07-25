import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = driver =webdriver.Chrome("D:\\chromedriver_win32 (5)\\chromedriver.exe")
driver.get("https://demo.automationtesting.in/window.html")
driver.maximize_window()
ele1 = driver.find_element_by_xpath("//a[text() = 'SwitchTo']")
ele2 = driver.find_element_by_xpath("//a[text() = 'Frames']")
time.sleep(5)
ActionChains(driver).move_to_element(ele2).click().perform()
time.sleep(5)
driver.find_element_by_xpath("//a[@class = 'analystic'])[2]").click()
time.sleep(5)
eleframe1 = driver.find_element_by_xpath("//div[@id ='Multiple')/iframe")
driver.switch_to_frame(eleframe1)
eleframe2 = driver.find_element_by_xpath("//div[@class = 'row']/iframe")
driver.switch_to_frame(eleframe2)
time.sleep(5)
driver.find_element_by_xpath("//input[@type = 'text']").send_keys("kartik")
time.sleep(5)
