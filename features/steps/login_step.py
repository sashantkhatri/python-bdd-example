from behave import *
from selenium.common.exceptions import TimeoutException
import allure

@allure.step('User has navigated to login page')
@Given('User has navigated to login page')
def step_impl(context):
    print("User has navigated to login page")

    try:
        if context.login_page.get_element(context.driver,
                    context.login_page_locators.SIGN_ON).is_displayed() :
            context.login_page.get_element(context.driver,
                    context.login_page_locators.SIGN_ON).click()
    except TimeoutException :
        context.flight_finder_page.get_element(context.driver,
                    context.flight_finder_page_locators.SIGN_OFF).click()

@When('User enters username as {username} and password as {password} to login')
def step_impl(context, username, password):
    print("User performs login")
    context.login_page.do_login( context.driver, username, password)


@Then('User should be on flight finder page')
def step_impl(context):
    print("User should be on flight finder page")
    context.flight_finder_page.is_page_open(context.driver)

@Then('User should be on flight finder page If entered credentials are {is_valid}')
def step_impl(context, is_valid):

    if is_valid=="True" :
        context.flight_finder_page.is_page_open(context.driver)
        context.flight_finder_page.perform_sign_off(context.driver)
    else:
        context.login_page.is_page_open(context.driver)