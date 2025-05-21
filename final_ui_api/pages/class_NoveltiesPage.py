import allure
from selenium.webdriver.common.by import By

@allure.epic("Кинопоиск")
@allure.suite("NoveltiesPage")
class NoveltiesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://hd.kinopoisk.ru/selection/novelties"

    def open(self):
        self.driver.get(self.url)


    def click_element(self, numb: int):
        elements = self.driver.find_elements(
            By.CLASS_NAME, "ListItem_selection-card__MeC9v")

        if len(elements) >= numb:
            # Выбираем элемент по указанному номеру и кликаем
            element_to_click = elements[numb]
            element_to_click.click()
        else:
            raise IndexError(f"Элемент с номером {numb} отсутсвует.")

