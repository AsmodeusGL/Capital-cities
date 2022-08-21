import requests

from bs4 import BeautifulSoup
from urllib.parse import quote


class Main:
    def __init__(self, url) -> None:
        self.url = url

    def main(self) -> None:
        response = requests.get(url=self.url)
        print(response.text)


if __name__ == '__main__':
    Main(f'https://ru.wikipedia.org/wiki/{quote("Список_столиц_государств")}').main()
