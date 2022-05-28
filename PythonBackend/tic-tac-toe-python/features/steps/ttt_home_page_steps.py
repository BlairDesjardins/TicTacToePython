import unittest

from behave import when, then, given

from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.home_page import TicTacToeHome


# Scenario 1
@given('The user is on the log in page')
def user_gets_to_login_page(context):
    driver: WebDriver = context.driver
    driver.get('file:///C:/Users/17146/Desktop/TicTacToeApp/TicTacToeFrontend/login.html')


@when('The user inputs their username')
def user_logs_in(context):
    home_page: TicTacToeHome = context.home_page
    home_page.username().send_keys("blair")


@when('The user inputs their password')
def user_types_password(context):
    home_page: TicTacToeHome = context.home_page
    home_page.password().send_keys("password")


@when('The user presses log in')
def user_presses_login(context):
    home_page: TicTacToeHome = context.home_page
    home_page.login().click()


@then('The user should be on the main game page')
def log_in_successful(context):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.title, 'Tic Tac Toe')

# -------------------------------------------------------------------------------------------------------

# Scenario 2
# @given('The user is on the log in page')
# def user_gets_to_login_page():

# @when('The user inputs their username incorrectly')
# def user_does_not_log_in():
#
# @then('The user should be on the log in page')
# def log_in_fails():
