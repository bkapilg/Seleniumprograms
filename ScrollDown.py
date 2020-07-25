from selenium import webdriver
import time

driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
driver.get('https://www.flipkart.com/')
time.sleep(10)
driver.execute_script("window.scrollTo(0,3500)")
# driver.close()
