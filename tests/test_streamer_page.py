from config.config import BASE_URL
from pages.main_page import MainPage


def test_search_bar(page):
    main_page = MainPage(page)
    main_page.navigate(BASE_URL)
    main_page.search_for_streamers("LOL")
