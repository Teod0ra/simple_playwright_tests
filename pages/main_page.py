from pages.base_page import BasePage


class MainPage(BasePage):

    def go_to_search_page(self):
        search_page = self.page.locator('a:has-text("Browse")')
        search_page.click()
        self.page.wait_for_load_state("domcontentloaded")
        from pages.search_page import SearchPage
        return SearchPage(self.page)
        
