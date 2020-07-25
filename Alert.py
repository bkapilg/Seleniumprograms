import time
from telnetlib import EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
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
time.sleep(3)
driver.find_element_by_xpath("//a[text()='Alert with Textbox ']").click()
time.sleep(5)
driver.find_element_by_xpath("//button[@onclick= 'promptbox()']").click()

#driver.find_element_by_xpath('//a[@href="#OKTab"]').click()


try:
    WebDriverWait(driver,5).until(EC.alert_is_present(), 'Timed out waitning for alert to appear')
    alert = driver.switch_to.alert
    alert.send_keys('karthik')
    #alert.dismiss()
    print("text entered")
except TimeoutException:
       print("no alert")
