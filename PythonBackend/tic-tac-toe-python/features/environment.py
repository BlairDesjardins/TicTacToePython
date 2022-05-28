import unittest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

# This file is used by behave to do some background setup including an object we'll need
# (called the Context Object) but it also is a designated place to add any setup and teardown
# functions that we want for our tests
# These functions must be named using behave's conventions
from features.pages.home_page import TicTacToeHome


def before_all(context):
    driver: WebDriver = webdriver.Chrome(
        'C:/Users/17146/PycharmProjects/pythonProject/Selenium Example/chromedriver.exe')
    home_page = TicTacToeHome(driver)

    test = unittest.TestCase()

    context.driver = driver
    context.home_page = home_page
    context.unittest = test
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
