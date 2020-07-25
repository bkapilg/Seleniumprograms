from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.remote.webelement import WebElement

driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")

driver.get("https://www.irctc.co.in/nget/profile/user-registration")
time.sleep(5)
driver.find_element_by_xpath("//button[@class='btn btn-primary'][1]").click()
driver.find_element_by_name("userName").send_keys("Abcde1234")
driver.find_element_by_name("usrPwd").send_keys("Abcde1234")
driver.find_element_by_name("cnfUsrPwd").send_keys("Abcde1234")
driver.find_element_by_xpath("//label[text()='Select Security Question']").click()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='What is your pet name?']").click()
driver.find_element_by_xpath("//input[@placeholder='Security Answer']").send_keys("dog")
time.sleep(2)
driver.find_element_by_xpath("//label[text()='Select Preferred Language']").click()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='English']").click()
time.sleep(5)
driver.find_element_by_id("firstName").send_keys("kartik")
driver.find_element_by_id("lastname").send_keys("gupta")
driver.find_element_by_xpath("//input[@id='M']").click()
#driver.find_element_by_xpath("//label[text()='Select Occupation')]").click()
#driver.find_element_by_xpath("//span[text()='PUBLIC']").click()
#driver.find_element_by_xpath("//input[text()=' Unmarried')]").click()
#driver.find_element_by_link_text("Select city").click()
#driver.find_element_by_link_text(("Select a Post Office")).click()
driver.find_element_by_id("email").send_keys("kartikeybarsainya101@gmail.com")
driver.find_element_by_id("mobile").send_keys("9066300895")
obj = Select(driver.find_element_by_xpath("//select[@formcontrolname='nationality']"))
obj.select_by_index(1)
time.sleep(4)
obj1 = Select(driver.find_element_by_xpath("//select[@formcontrolname='resPostOff']"))
obj.select_by_index(2)
driver.find_element_by_id("resAddress1").send_keys("maratalli")
driver.find_element_by_id("resAddress2").send_keys("belundur")
driver.find_element_by_id("resAddress3").send_keys("dmart")
driver.find_element_by_name("resPinCode").send_keys("560045")
driver.find_element_by_id("resState").send_keys("karnatka")
driver.find_element_by_id("resPhone").send_keys("9066300895")
obj2 = Select(driver.find_element_by_xpath("//select[@formcontrolname='resCity']"))
obj2.select_by_index(1)
time.sleep(5)
obj3 = Select(driver.find_element_by_xpath("//select[@formcontrolname='resPostOff']"))
obj3.select_by_index(2)
time.sleep(5)
driver.find_element_by_xpath("//input[@value='y']").click()
# checkbox = driver.find_element_by_id("sbi")
# checkbox.click()
time.sleep(10)
driver.find_element_by_xpath("//input[@formcontrolname='termCondition']").click()

driver.find_element_by_link_text("REGISTER").click()





