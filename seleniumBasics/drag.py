from  selenium import webdriver
from  selenium.webdriver import ActionChains
driver =webdriver.Chrome("D:\\chromedriver_win32 (5)\\chromedriver.exe")
driver.get("http://demo.guru99.com/test/drag_drop.html")
driver.maximize_window()
from1 =driver.find_element_by_xpath("//a[@class ='block13 ui-draggable'])[1]")
to1 = driver.find_element_by_xpath("//ol[@class = 'field14 ui-droppable ui-sortable'])[3]")
ActionChains(driver).drag_and_drop("from1,to1").click().perform()
#ActionChains(driver).drag_and_drop(from1,to1).click().perform()
#from1 = driver.find_element_by_xpath("(//a[@class = 'button button-orange'])[4]")
