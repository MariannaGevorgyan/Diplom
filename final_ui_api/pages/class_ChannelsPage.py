import allure
from pytest_selenium import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Кинопоиск")
@allure.suite("ChannelsPage")
class ChannelsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://hd.kinopoisk.ru/channels"


    def open(self, driver):
        self.driver.get(self.url)


    def back_homepage(self, driver):
        logo = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(By.CLASS_NAME, 'styles_logo__1R5HL'))
        )
        logo.click()