from selenium import  webdriver
import time


driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
ele1 = driver.find_element_by_xpath("//a[text() = 'SwitchTo']")
ele2 = driver.find_element_by_xpath("//a[text()= 'Windows']")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()
time.sleep(10)
newtab = driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_link_text("Contact").click()
driver.find_element_by_id("name").send_keys("kartik")
driver.find_element_by_id("email").send_keys("kartikeybarsainya101@gmail.com")
driver.find_element_by_id("subject").send_keys("abc")
driver.find_element_by_id("message").send_keys("hi")
driver.find_element_by_id("contact-form").click()
#driver.find_element_by_link_text("Contact").click()



