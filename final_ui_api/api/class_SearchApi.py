import requests
import allure


@allure.epic("Кинопоиск")
@allure.suite("SearchApi")
class SearchApi:
    def __init__(self, base_url: str, token) -> None:
        self.base_url = base_url
        self.token = token

    def get_search_to_name(self, name_movi) -> dict:
        """Поиск фильма по названию через API
        """
        path = (
            "{url}v1.4/movie/search?page=1&limit=1&query={name}".
            format(url=self.base_url, name=name_movi)

        )
        headers = {
            "x-API-KEY": self.token,
            "accept": "application/json"
        }

        response = requests.get(path, headers=headers)
        return response.json()


    def get_search_to_data(self, data_realse, params=None) -> dict:
        """ Поиск фильмов по дате релиза, через API
        """
        path = ("{url}v1.4/movie/random?premiere.russia={data}".
                format(url=self.base_url, data=data_realse))
        headers = {
            "X-API-KEY": self.token,
            "accept": "application/json"
        }
        response = requests.get(path, params=params, headers=headers)
        return response.json()


    def get_search_to_age(self) -> dict:
        """Получение списков фильмов с возрастом от 18+
        """
        path = "{url}v1.4/movie".format(url=self.base_url)
        headers = {
            "X-API-KEY": self.token,
            "accept": "application/json"
            }
        params = {
            "page": "3",
            "limit": "10",
            "ageRating": "!18"
        }
        response = requests.get(path, params=params, headers=headers)
        return response.json()


    def get_search_to_year(self) -> dict:
        """Список фильмов выпущенные в конкретном году используя API
        """
        params = {
            "pages": "3",
            "limit": "10",
            "year": "2000"
        }
        path = "{url}v1.4/movie".format(url=self.base_url)
        headers = {"X-API-KEY": self.token}
        response = requests.get(path, params=params, headers=headers)
        return response.json()


    def get_search_to_rating(self) -> dict:
        """Список фильмов с определенным диапозоном рейтинга (от 8 до 10 баллов)
        """
        params = {
            "page": "3",
            "limit": "10",
            "rating.kp": "8-10"
        }
        path = "{url}v1.4/movie".format(url=self.base_url)
        headers = {"X-API-KEY": self.token}
        response = requests.get(path, params=params, headers=headers)
        return response.json()