import json
import re

import requests
from bs4 import BeautifulSoup

from src.packages.utils import PathStorage


class Data:

    def save_data(self, data, name_path, mode="w"):
        path = PathStorage.get_path_to_data() / name_path
        with open(path, mode=mode, encoding='utf-8') as save_in_json:
            json.dump(data, save_in_json, ensure_ascii=False)
        print("Saving successfully!!!")

    def load_data(self, name_path, mode="r"):
        path = PathStorage.get_path_to_data() / name_path
        with open(path, mode=mode, encoding='utf-8') as json_load:
            data = json.load(json_load)
        return data


class FindContent(Data):
    """
    Site parser 'https://www.kinopoisk.ru/'
    url, headers, cookies take from the site
    """

    def __init__(self, url, headers, cookies):
        self.url = url
        self.headers = headers
        self.cookies = cookies

    @classmethod
    def validate_country_genre_director(cls, data: str) -> list:
        if "Корея" in data:
            data = data.replace("• ", '').replace("\xa0\xa0", " ").split(" ")
            new_data = [" ".join(data[:2])] + data[2:]
            return new_data
        else:
            return data.replace("• ", '').replace("\xa0\xa0", " ").split(" ")

    @classmethod
    def validate_year_duration(cls, data: str) -> list:
        return data.replace(", ", " ").replace("\xa0", " ").strip().split(" ")

    @classmethod
    def search_trailer(cls, title: str, year: str) -> str:
        search_query = (title + " " + year).replace(" ", "+") + "+трейлер"
        url = f"https://www.youtube.com/results?search_query={search_query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        links = soup.find_all('script')
        url_trailer = "https://www.youtube.com/watch"
        for link in links:
            search_link = re.findall(r'"/watch(.*?)"', link.text)
            if len(search_link) > 1:
                url_trailer += search_link[0]
                break
        return url_trailer

    def get_pages(self) -> list:
        response = requests.get(self.url, headers=self.headers, cookies=self.cookies)
        soup = BeautifulSoup(response.text, "lxml")
        pages = soup.find("div", "styles_root__AT6_5 styles_root__RoFSb").find_all("a")
        links = list(map(lambda x: self.url + x.split("/")[-1], [link['href'] for link in pages]))
        return links

    def get_data(self, first_page=1, last_page=1, count_content=0) -> dict:
        count_content = count_content
        data_content = {}
        for page in range(first_page, last_page + 1):
            response = requests.get(self.url + f"?page={page}", headers=self.headers, cookies=self.cookies)
            soup = BeautifulSoup(response.text, "lxml")
            content_full_data = soup.find_all('div', "styles_upper__j8BIs")
            for data in content_full_data:
                count_content += 1
                title = data.find("span", "styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj").text.strip()
                genre = self.validate_country_genre_director(
                    data.find("span", "desktop-list-main-info_truncatedText__IMQRP").text)[1].strip()
                director = " ".join(self.validate_country_genre_director(
                    data.find("span", "desktop-list-main-info_truncatedText__IMQRP").text)[3:]).strip()
                country = self.validate_country_genre_director(
                    data.find("span", "desktop-list-main-info_truncatedText__IMQRP").text)[0].strip()
                year = \
                    self.validate_year_duration(data.find("span", "desktop-list-main-info_secondaryText__M_aus").text)[
                        0].strip()
                duration = " ".join(
                    self.validate_year_duration(data.find("span", "desktop-list-main-info_secondaryText__M_aus").text)[
                    1:]).strip()
                if data.find("span",
                             "styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg styles_top250Type__mPloU") is not None:
                    rating = data.find("span",
                                       "styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg styles_top250Type__mPloU").text.strip()
                elif data.find("span", "styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg") is not None:
                    rating = data.find("span",
                                       "styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg").text.strip()
                elif data.find("span", "styles_kinopoiskValueNeutral__sW9QT styles_kinopoiskValue__9qXjg"):
                    rating = data.find("span",
                                       "styles_kinopoiskValueNeutral__sW9QT styles_kinopoiskValue__9qXjg").text.strip()
                else:
                    rating = data.find("span",
                                       "styles_kinopoiskValueNegative__Y75Rz styles_kinopoiskValue__9qXjg").text.strip()

                trailer = self.search_trailer(title, year)
                content = {
                    f"{count_content}": {
                        "title": title,
                        "genre": genre,
                        "director": director,
                        "country": country,
                        "year": year,
                        "duration": duration,
                        "rating": rating,
                        "trailer": trailer
                    }
                }
                data_content.update(content)
                print(content)
        return data_content


class FindJokes(Data):
    """
    Site parser "https://ru-fun.ru/hits" and "https://anekdotbar.ru/top-100.html"
    """

    def __init__(self, url):
        self.url = url

    @classmethod
    def validate_text(cls, data: str) -> str:
        reg_1 = re.findall(r"\n.+\n[-+?]\d+", data)
        reg_2 = set(re.findall(r"([^0-9а-яА-ЯёЁ ]-|[^0-9а-яА-ЯёЁ -][а-яА-ЯёЁ])", data))
        if reg_1:
            data = data.strip("\n").strip().replace("\r", "").replace(reg_1[0], "")
            if reg_2:
                data = data.replace("\n\n", "").replace("\n", "")
                for value in reg_2:
                    data = data.replace(value, value[0] + "\n" + value[1])
            return data.replace("\n\n", "\n")
        return data.strip("\n").strip().replace("\r", "").replace("\n\n", "\n")

    def get_data(self, attribute, count_content=0) -> dict:
        count_content = count_content
        data_content = {}
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "lxml")
        content_full_data = soup.find_all('div', attribute)
        for data in content_full_data:
            count_content += 1
            content = {
                f"{count_content}": self.validate_text(data.find("p").text if data.find("p") is not None else data.text)
            }
            data_content.update(content)
            print(content)
        return data_content


if __name__ == "__main__":
    headers = {
        "Content-Type": "",
        "User-Agent": ""
    }
    cookies = {
        "Cookie": ""
    }
    film = True
    anecdote = False
    anecdote_next = False

    if film:
        url_film = "https://www.kinopoisk.ru/lists/movies/genre--anime/"
        film = FindContent(url_film, headers=headers, cookies=cookies)
        pages = film.get_pages()
        data = film.get_data(first_page=1, last_page=5)
        save = film.save_data(data, "anime.json")

    if anecdote:
        url = "https://ru-fun.ru/hits"
        anecdote = FindJokes(url)
        data = anecdote.get_data(attribute="post-item__text")
        save = anecdote.save_data(data, "jokes.json")

    if anecdote_next:
        url = "https://anekdotbar.ru/top-100-2.html"
        anecdote_next = FindJokes(url)
        data = anecdote_next.get_data(attribute="tecst", count_content=100)
        open_json = anecdote_next.load_data("jokes.json")
        open_json.update(data)
        save = anecdote_next.save_data(open_json, "jokes.json")
