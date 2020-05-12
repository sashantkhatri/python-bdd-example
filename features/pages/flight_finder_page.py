from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlightFinderPageLocator(object):
    # Search Results Page Locators
    SIGN_OFF = ['XPATH', '//a[contains(text(), "SIGN-OFF")]']
    FLIGHT_DETAILS_LBL = ['XPATH', '//form[@name=\'findflight\']//font[contains(text(),"Flight")]']
    PASSENGERS_COUNT = ['XPATH', '//select[@name=\'passCount\']']
    DEPARTING_FROM = ['XPATH', '//select[@name=\'fromPort\']']


class FlightFinderPage():
    # Search Results Page Actions

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

    def get_page_title(self, driver):
        return self.driver.title

    def is_page_open(self, driver):
        flight_detail_lbl = self.get_element(driver, FlightFinderPageLocator.FLIGHT_DETAILS_LBL)
        passengers_count = self.get_element(driver, FlightFinderPageLocator.PASSENGERS_COUNT)
        departing_from = self.get_element(driver, FlightFinderPageLocator.DEPARTING_FROM)

        assert flight_detail_lbl.is_displayed(), True
        assert passengers_count.is_displayed(), True
        assert departing_from.is_displayed(), True

    def perform_sign_off(self, driver):
        sign_off = self.get_element(driver, FlightFinderPageLocator.SIGN_OFF)
        sign_off.click()