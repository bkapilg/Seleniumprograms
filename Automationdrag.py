from selenium import  webdriver
import time

from selenium.webdriver import ActionChains

driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Static.html")
color = driver.find_element_by_partial_link_text("Register").get_attribute("color")
print(color)
# from1=driver.find_element_by_id("angular")
# to1=driver.find_element_by_class_name("dragged")
# ActionChains(driver).drag_and_drop(from1,to1).click().perform