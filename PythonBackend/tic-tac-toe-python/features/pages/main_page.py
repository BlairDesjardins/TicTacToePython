from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TicTacToeMain:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def start_game(self):
        return self.driver.find_element(By.ID, value='')

    def play_game(self):
        return self.driver.find_element(By.ID, value='')

    def end_game(self):
        return self.driver.find_element(By.ID, value='')

