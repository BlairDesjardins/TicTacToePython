from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TicTacToeHome:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username(self):
        return self.driver.find_element(By.ID, value="Uname")

    def password(self):
        return self.driver.find_element(By.ID, value="password")

    def login(self):
        return self.driver.find_element(By.ID, value="login")
