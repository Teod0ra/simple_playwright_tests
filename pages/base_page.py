import os
import datetime


class BasePage:
    def __init__(self, page):
        self.page = page

    def find_element(self, selector: str):
        return self.page.locator(selector)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def fill(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.fill(text)

    def navigate(self, url):
        self.page.goto(url)

    def take_screenshot(self, filename="screenshot.png"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{filename}_{timestamp}.png"
        path = os.path.join("reports", "screenshots", filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.page.screenshot(path=path)
        return path

    def accept_cookies_if_present(self):
        accept_btn = self.page.locator(
            '[data-a-target="consent-banner-accept"]')
        accept_btn.wait_for(state="visible")
        accept_btn.click()

    def scroll_down(self, times=1):
        for _ in range(times):
            self.page.evaluate("window.scrollBy(0, window.innerHeight);")

    def wait_for_fully_loaded_stream(self):
        self.page.wait_for_function(""" () => {
        const video = document.querySelector('video');
        return video && !video.seeking && !video.paused; }
        """, timeout=30000)
