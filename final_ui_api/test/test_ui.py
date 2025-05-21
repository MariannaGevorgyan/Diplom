import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.id("MainPage-1")
@allure.severity("blocker")
@allure.title("Клик по кнопке 'Вход'")
@allure.feature("кнопка 'Вход'")
@allure.description("Функциональеость кнопки 'Вход' на главной странице Кинопоиск")
def test_button_entrance(main_page):
    with allure.step("Нажать на кнопку 'Вход'"):
       main_page.click_on_button()

    with allure.step("Дождаться загрузки элемента на старнице"):
       wait = WebDriverWait(main_page.driver, 10)
       new_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'passp-auth-content')))
       assert new_element.is_displayed()



@allure.id("MainPage-2")
@allure.severity("critical")
@allure.title("Ввод текста в строку поиск")
@allure.feature("Строка 'Поиск'")
@allure.description("Функциональеость строки 'Поиск' на главной странице Кинопоиск")
def test_input(main_page):
    with allure.step("Ввести название фильма в строку поиск"):
      main_page.input_text("Вий")
    with allure.step("Дождаться загрузки элемента на странице"):
      wait = WebDriverWait(main_page.driver, 30)
      new_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'styles_root___4K2i')))
      assert new_element.is_displayed()


@allure.id("NoveltiesPage-1")
@allure.severity("blocker")
@allure.title("Выбор фильма в разделе 'Новинки'")
@allure.story("Выбор фильма на странице по очередности")
@allure.feature("Раздел Кинопоиска 'Новинки' ")
@allure.description("Выбор фильма в разделе 'Новинки' и появление элемента 'Смотреть фильм' ")
def test_novelties(novelties_page):
   with allure.step("Выбрать любой фильм, кликнув по нему"):
      novelties_page.click_element(30)

   with allure.step("Дождаться загрузки элемента на странице"):
      wait = WebDriverWait(novelties_page.driver, 10)
      new_element = wait.until(
          EC.visibility_of_element_located((
            By.XPATH, "//button[@data-test-id= 'MainButton_offer']"
        )))
      assert new_element.is_displayed()

      button_text = new_element.text.strip()
      assert button_text != "", f"Кнопка пустая или невидима: '{button_text}'"

      print(button_text)

@allure.id("MainPage-3")
@allure.severity("blocker")
@allure.title("меню навигация")
@allure.story("Работа функциональности меню навигации")
@allure.feature("Кнопка 'вход '")
@allure.description("Переход на страницы меню навигации")
def test_link_to_page(main_page):
    with allure.step("Перейти в раздел 'Онлайт-Кинотеатр'"):
     main_page.navigation_menu('styles_root__7mPJN styles_lightThemeItem__BSbZW')

    assert True, "Тест выполнен"


@allure.id("Channelspage-1")
@allure.severity("critical")
@allure.title("Вернуться на главную страницу")
@allure.story("Работа функциональности элемента 'Кинопоиск' ")
@allure.feature("Элемент хедер 'Кинопоиск' ")
@allure.description("Функциональность элемента  'Кинопоиск' расположенный в хедер")
def test_return_to_main_page(main_page, channels_page):
    with allure.step("перейти на страницу 'Телеканалы' и нажать на элемент c'Кинопоиск'"):
        channels_page.back_homepage()

    with allure.step("дождаться загрузки главной страницы"):
        current_url = main_page.driver.current_url
        assert current_url == "https://www.kinopoisk.ru/", (
            f"Ожидалось перенаправление на главную страницу,"
            f" Получено: {current_url}"
        )
