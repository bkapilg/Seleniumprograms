import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium import  webdriver
import  time
driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
driver.get("http://facebook.com")
driver.maximize_window()
time.sleep(3)
ele1=driver.find_element_by_xpath("//span[text()='Create an account']").value_of_css_property('color')
print(ele1)# ele2=driver.find_element_by_xpath("//a[text()='Alerts']")# ActionChains(driver).move_to_element(ele1).move_to_element(ele2).click().perform# time.sleep(5)# print(color)
# ele1.hex
test = hex(ele1)
print(test)
# time.sleep(3)
# driver.switch_to.alert.accept()


# driver.find_element_by_xpath("//button[@onclick= 'confirmbox()']").click()

