import time
import time
class LoginPage():

def __init__(self, driver):
    self.driver = driver

    self.log_xpath = "//span[text()='Log In']"
    self.username_textbox_xpath = "//input[@placeholder='E-mail address']"
    self.password_textbox_xpath = "//input[@placeholder='Password']"
    self.login_button_xpath = "//div[text()='Login']"


def click_logininhome(self):
    time.sleep(5)
    self.driver.find_element_by_xpath(self.log_xpath).click()


def enter_username(self, username):
    self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
    self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)


def enter_password(self, password):
    self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
    self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)
    time.sleep(5)


def click_loginbutton(self):
    self.driver.find_element_by_xpath(self.login_button_xpath).click()
    time.sleep(5)


