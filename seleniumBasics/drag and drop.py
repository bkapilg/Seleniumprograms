from  selenium import webdriver
from  selenium.webdriver import  ActionChains
import  time
driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
driver.get("http://demo.guru99.com/test/drag_drop.html")
driver.maximize_window()
from1 = driver.find_element_by_xpath("(//a[@class='button button-orange'])[4]")
to1= driver.find_element_by_xpath("(//ol[@class='field13 ui-droppable ui-sortable'])[2]")
#ActionChains(driver).drag_and_drop(from1,to1).click().perform()
ActionChains(driver).drag_and_drop(from1,to1).click().perform()
driver.close()
