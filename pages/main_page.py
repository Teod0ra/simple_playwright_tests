from pages.base_page import BasePage


class MainPage(BasePage):

    search_bar = 'input[autocomplete="twitch-nav-search"]'

    def search_for_streamers(self, text):
        self.fill(self.search_bar, text)
        self.page.press("[autocomplete='twitch-nav-search']", "Enter")
