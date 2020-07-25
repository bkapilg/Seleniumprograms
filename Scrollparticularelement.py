from selenium import webdriver
import time
driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
driver.get('https://www.flipkart.com/')
time.sleep(10)
vv= driver.find_element_by_link_text("Brand Directory")
driver.execute_script("arguments[0].scrollntoView();", vv)
