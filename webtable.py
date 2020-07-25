from selenium import webdriver
import  time

driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
driver.get("file:///C:/Users/20126635/Documents/demo.html")
rows=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))#count number of row
cols=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))#count number of column
print(rows)
print(cols)
print("product"+"  "+"Article"+"   "+"price")
for r in range(2,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='     ')
    print()