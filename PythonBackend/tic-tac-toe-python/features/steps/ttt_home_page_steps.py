import time
import unittest

from behave import when, then, given
from selenium.common import TimeoutException

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.pages.home_page import TicTacToeHome


# Scenario 1
@given('The user is on the log in page')
def user_gets_to_login_page(context):
    driver: WebDriver = context.driver
    # driver.get('file:///C:/Users/17146/Desktop/TicTacToeApp/TicTacToeFrontend/login.html')
    driver.get('C:/Users/blair/Documents/Revature/TicTacToeFrontend/login.html')


@when('The user inputs their username')
def user_logs_in(context):
    home_page: TicTacToeHome = context.home_page
    home_page.username().send_keys("blair")


@when('The user inputs their password')
def user_types_password(context):
    home_page: TicTacToeHome = context.home_page
    home_page.password().send_keys("password")


@when('The user inputs their password incorrectly')
def user_types_password_incorrectly(context):
    home_page: TicTacToeHome = context.home_page
    home_page.password().send_keys("password123")


@when('The user presses log in')
def user_presses_login(context):
    home_page: TicTacToeHome = context.home_page
    home_page.login().click()


@then('The user should be on the main game page')
def log_in_successful(context):
    try:
        WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.ID, 'players')))
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        test: unittest.TestCase = context.unittest
        test.assertEquals(context.driver.title, 'Tic Tac Toe')


@then('The user should be on the log in page')
def log_in_unsuccessful(context):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.title, 'Login')
