import HtmlTestRunner
from selenium import webdriver
import unittest
import time
import pytest


import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))

from POMProjectDemo.Pages.loginPage import LoginPage
from POMProject.Pages.Homepage import HomePage



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
        cls.driver.maximize_window()


    def test_a_login_valid(self):
        driver = self.driver
        driver.get("https://freecrm.com/")
        login = LoginPage(driver)
        login.click_logininhome()
        login.enter_username("sairamboopathi@gmail.com")
        login.enter_password("Sairam@123")
        login.click_loginbutton()



        homepage = HomePage(driver)
        homepage.click_Contact()
        homepage.clickHomelogoutButton()
        homepage.clickLogout()

    def test_b_login_invalid(self):
        driver = self.driver
        driver.get("https://freecrm.com/")
        login = LoginPage(driver)
        login.click_logininhome()
        login.enter_username("sairamboopathi@gmail.com")
        login.enter_password("sairam@1234")
        login.click_loginbutton()

    def test_c_forget_your_password(self):
        self.driver.find_element_by_partial_link_text('Forgot your password').click()
        self.driver.find_element_by_id('email').sendkeys("sairamboopathi@gmail.com")
        time.sleep(5)
        self.driver.find_element_by_partial_link_text('Reset password').click()

        # homepage = HomePage(driver)
        # homepage.click_companies()
        # homepage.click_products()
        # homepage.clickHomelogoutButton()

        if __name__ == '__main__':
         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output='/Users/rcwboat/PycharmProjects/SeleniumPrgms/POMProject/reports'))

