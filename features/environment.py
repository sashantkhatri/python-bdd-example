from features.pages.login_page import LoginPage, LoginPageLocator
from features.pages.flight_finder_page import FlightFinderPage, FlightFinderPageLocator
from selenium import webdriver
import allure


def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://newtours.demoaut.com/")
    context.driver.maximize_window()
    context.login_page = LoginPage()
    context.login_page_locators = LoginPageLocator()
    context.flight_finder_page = FlightFinderPage()
    context.flight_finder_page_locators = FlightFinderPageLocator()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
                      name='screenshot',
                      attachment_type=allure.attachment_type.PNG)


def after_all(context):
    context.driver.close()