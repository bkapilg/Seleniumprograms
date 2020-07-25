from  selenium import  webdriver
import  time

from selenium.webdriver import ActionChains

driver =webdriver.Chrome("D:\\chromedriver_win32 (5)\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
time.sleep(10)
#driver.find_element_by_class_name("dropdown-toggle").click()
ele1 = driver.find_element_by_partial_link_text("Interactions").click()
time.sleep(3)
ele2 = driver.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[6]/ul/li[1]/a").click()
ele3 = driver.find_element_by_xpath('//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]/a').click()
#ele3 = driver.find_element_by_xpath("//a[text() = 'Static']")
time.sleep(10)
actionChains = ActionChains(driver)


from1 =driver.find_element_by_id("angular")
to1 = driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div")
actionChains.drag_and_drop(from1, to1).perform()
# ActionChains(driver).drag_and_drop(from1, to1).click().perform()

#ActionChains(driver).move_to_element(ele1).move_to_element(ele2).click().perform()