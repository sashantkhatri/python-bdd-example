from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageLocator(object):
    # Home Page Locators
    SIGN_ON = ['XPATH', '//a[contains(text(), "SIGN-ON")]']
    REGISTER = ['XPATH', '//a[contains(text(), "REGISTER")]' ]
    USERNAME_TXT = ['NAME',"userName"]
    PASSWORD_TXT = ['NAME', 'password']
    SUBMIT = ['NAME', 'login']

class LoginPage():
    # Home Page Actions
    #
    def get_element(self, driver, locator):
        locator_type = locator[0]
        locator_value = locator[1]
        if locator_type=="XPATH" :
            locator_type = By.XPATH
        else :
            locator_type = By.NAME
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )
        locator_type = locator[0]
        locator_value = locator[1]
        if locator_type.__contains__('XPATH'):
            return driver.find_element_by_xpath(locator_value)
        else :
            return driver.find_element_by_name(locator_value)

    def navigate_to_login_page(self):
        self.get_element(LoginPageLocator.SIGN_ON).click()

    def is_page_open(self, driver):
        username= self.get_element(driver, LoginPageLocator.USERNAME_TXT)
        password = self.get_element(driver, LoginPageLocator.PASSWORD_TXT)
        submit = self.get_element(driver, LoginPageLocator.SUBMIT)
        assert username.is_displayed(), True
        assert password.is_displayed(), True
        assert submit.is_displayed(), True

    def do_login(self, driver, username, password):
        self.is_page_open(driver)
        username_txt = self.get_element(driver, LoginPageLocator.USERNAME_TXT)
        username_txt.send_keys(username)
        password_txt = self.get_element(driver, LoginPageLocator.PASSWORD_TXT)
        password_txt.send_keys(password)
        submit_btn = self.get_element(driver, LoginPageLocator.SUBMIT)
        submit_btn.click()