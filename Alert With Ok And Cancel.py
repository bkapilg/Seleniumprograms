import time
from telnetlib import EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium import  webdriver
import  time
driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
time.sleep(10)
ele1=driver.find_element_by_xpath("(//a[@class='dropdown-toggle'])[1]")
ele2=driver.find_element_by_xpath("//a[text()='Alerts']")
ActionChains(driver).move_to_element(ele1).move_to_element(ele2).click().perform()
time.sleep(10)
driver.find_element_by_partial_link_text('Cancel').click()
time.sleep(5)
driver.find_element_by_xpath("//button[@onclick= 'confirmbox()']").click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(8)
driver.find_element_by_xpath("//button[@onclick= 'confirmbox()']").click()
driver.switch_to.alert.dismiss()
#alert.dismiss()

