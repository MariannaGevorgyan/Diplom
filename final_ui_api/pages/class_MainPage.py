import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.epic("Кинопоиск")
@allure.suite("MainPage")
class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.kinopoisk.ru"

    def open(self):
        self.driver.get(self.url)

    def click_on_button(self):
        button = self.driver.find_element(
            By.CLASS_NAME, 'styles_loginButton__LWZQp')
        button.click()

    def input_text(self,text):
        input_text = self.driver.find_element(By.CSS_SELECTOR, "input")
        input_text.click()
        input_text.send_keys(text)


    def navigation_menu(self,class_names):
        elements = self.driver.find_elements(By.CLASS_NAME, class_names)
        for element in elements:
            element.click()
        self.driver.back()


    def back_to_img(self, any_page_css):
        element_img = self.driver.find_element(By.CSS_SELECTOR, any_page_css)
        element_img.click()
        img = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'img.Tz6jKbE7Yc1fjK09M1sa.kinopoisk-header-logo__img'))
        )
        img.click()