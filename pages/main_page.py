from pages.base_page import BasePage


class MainPage(BasePage):

    def navigate_and_accept_cookies(self):
        self.navigate("https://www.twitch.tv")
        self.accept_cookies_if_present()

    def go_to_search_page(self):
        self.navigate_and_accept_cookies()
        search_page = self.page.get_by_role("link", name="Browse")
        search_page.click()
        self.page.wait_for_load_state("domcontentloaded")
        from pages.search_page import SearchPage
        return SearchPage(self.page)
