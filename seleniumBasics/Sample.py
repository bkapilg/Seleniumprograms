from selenium  import webdriver
import time
driver =webdriver.Chrome("D:\\chromedriver_win32 (5)\\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Register.html")


driver.find_element_by_xpath('//*[@placeholder="First Name"]').send_keys("john")
driver.find_element_by_xpath('//*[@placeholder="Last Name"]').send_keys("smith")
driver.find_element_by_xpath('//*[@ng-model="Adress"]').send_keys("marathalli")
time.sleep(1)
driver.find_element_by_xpath('//*[@ng-model="EmailAdress"]').send_keys("kartikeybarsainya12@gmail.com")
driver.find_element_by_xpath('//*[@ng-model="Phone"]').send_keys("9066300895")
driver.find_element_by_name("radiooptions").click()
driver.find_element_by_id("checkbox2").click()
# time.sleep(2)
#driver.find_element_by_xpath("//div[7]/div/multi-select/div[2]/ul/li[3]").click()
driver.find_element_by_id("firstpassword").send_keys("Abc@2020")
driver.find_element_by_id("secondpassword").send_keys("Abc@2121")
driver.find_element_by_id("submitbtn").click()


# #driver.find_element_by_class_name("form-control ng-pristine ng-valid-email ng-invalid ng-invalid-required ng-touched").send_keys("bangalore")
