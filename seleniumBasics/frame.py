from selenium import webdriver
from  selenium.webdriver import ActionChains
import  time

driver =webdriver.Chrome("D:\\chromedriver_win32 (5)\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
ele1 = driver.find_element_by_xpath("//a[text() = 'SwitchTo']")
ele2 = driver.find_element_by_xpath("//a[text() = 'Frames']")
time.sleep(10)
ActionChains(driver).move_to_element(ele1).move_to_element(ele2).click().perform()
#eleFrame1 =driver.find_element_by_xpath("//iframe[@name='SingleFrame']")
#driver.switch_to.frame(eleFrame1)
time.sleep(10)
eleFrame2 = driver.find_element_by_partial_link_text("Iframe").click()
# driver.switch_to.frame(eleFrame2)
driver.find_element_by_xpath("//input[@type='text']").send_keys("kartik")


