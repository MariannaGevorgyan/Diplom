import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from final_ui_api.pages.class_MainPage import MainPage
from final_ui_api.pages.class_NoveltiesPage import NoveltiesPage
from final_ui_api.pages.class_ChannelsPage import ChannelsPage
from final_ui_api.api.class_SearchApi import SearchApi


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(browser):
    page = MainPage(browser)
    page.open()
    browser.execute_script("window.scrollBy(0, 1000)")
    return page


@pytest.fixture
def novelties_page(browser):
    page = NoveltiesPage(browser)
    page.open()
    browser.execute_script("window.scrollBy(0, 1000)")
    return page

@pytest.fixture
def channels_page(browser):
    page = ChannelsPage(browser)
    page.open()
    browser.execute_script("window.scrollBy(0, 1000)")
    return page

@pytest.fixture
def auth_api():
    auth_api = SearchApi(
        base_url='https://api.kinopoisk.dev/',
        token='VJ1TE02-HTH4H71-HRDQ27K-SA1ZPRJ'
    )
    return auth_api