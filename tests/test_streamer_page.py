from config.config import BASE_URL
from pages.main_page import MainPage
from pages.search_page import SearchPage


def test_search_bar(emulator_configuration):
    main_page = MainPage(emulator_configuration)
    search_page = main_page.go_to_search_page()
    search_page.search_for_streamer_channels("StarCraft II")
    search_page.scroll_down(times=2)
    search_page.click_on_any_streaming_video()
    

