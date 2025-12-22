class BasePage:
    def __init__(self, page):
        self.page = page

    def find_element(self, locator):
        return self.page.locator(*locator)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def fill(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.fill(text)

    def navigate(self, url):
        self.page.goto(url)

    def take_screenshot(self, path):
        self.page.screenshot(path=path)
