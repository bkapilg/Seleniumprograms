import time

from selenium import  webdriver
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome("D:\\chromedriver_win32 (5)\\chromedriver.exe")
driver.get("http://www.newtours.demoaut.com/mercuryregister.php")
driver.maximize_window()
driver.find_element_by_name("firstName").send_keys("geet")
driver.find_element_by_name("lastName").send_keys("dj")
driver.find_element_by_name("phone").send_keys("3127466")
driver.find_element_by_name("userName").send_keys("gidghgeg@")
driver.find_element_by_name("address1").send_keys("edggwfget")
driver.find_element_by_name("city").send_keys("patna")
driver.find_element_by_name("state").send_keys("bihar")
# Select  = Select(driver.find_element_by_xpath(""))
#driver.find_element_by_xpath("//*[placeholder='Security Answer')]").click()
# sel = Select(eledropdown)
#sel.select_by_value("ARGENTINA")
#sel.select_by_index(2)
time.sleep(2)
eledropdown = driver.find_element_by_name("country")
sel=Select(eledropdown)
#select_by_visible_text("ANDORRA")
sel.select_by_visible_text("ARGENTINA")
# sel.select_by_index(2)
driver.find_element_by_id("email").send_keys("ssdnkd")
driver.find_element_by_name("password").send_keys("abc@38448")
driver.find_element_by_name("confirmPassword").send_keys("abc@38444")
driver.find_element_by_name("register").click()
#time.sleep(2)