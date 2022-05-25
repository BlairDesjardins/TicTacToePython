import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.home_page import TicTacToeHome
from features.pages.main_page import TicTacToeMain

ser = Service()
driver: WebDriver = webdriver.Chrome(service=ser)

home_page = TicTacToeHome(driver)
main_page = TicTacToeMain(driver)


def _test():
    try:
        driver.get("")
        time.sleep(3)
        home_page.login().send_keys("username")
        home_page.login().send_keys("password")
        home_page.login().click()
        time.sleep(3)
        main_page.start_game().click()
        main_page.play_game().click()
        main_page.end_game().click()
        time.sleep(3)

        assert "Game successfully played" == driver.switch_to.alert.text
    except AssertionError:
        print(f"Game could not be accessed - Request Failed\n Actual text: {driver.switch_to.alert.text}")
    else:
        print("Game was successfully accessed")
    finally:
        driver.quit()


if __name__ == '__main__':
    _test()
