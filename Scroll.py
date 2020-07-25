

from selenium import webdriver
import time

driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
driver.get('https://www.flipkart.com/')
time.sleep(10)
driver.execute_script("window.scrollTo(0,1800)","")    ##Particular pixel
# driver.close()















# import  time
# from  selenium import  webdriver
# driver =webdriver.Chrome("D:\chromedriver_win32 (6)\\chromedriver.exe")
#
# driver.get("https:/flipkart.com")
# driver.maximize_window()
# time.sleep(10)
# #driver.execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
# driver.execute_script("window.scrollTo(0, <vertical_position_to_scroll> )")
# driver.close()