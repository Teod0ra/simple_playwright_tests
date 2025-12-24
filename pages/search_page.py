from pages.base_page import BasePage
import re


class SearchPage(BasePage):

    search_input = 'input[placeholder="Search"]'

    def search_for_streamer_channels(self, text):
        self.page.fill(self.search_input, text)
        self.page.press(self.search_input, "Enter")
        button_view_all_results = self.page.locator(
            'p[aria-label="View All Channel Search Results"]')
        button_view_all_results.click()
        self.page.get_by_role("list").wait_for(state="visible")

    def click_on_any_streaming_video(self):
        streaming_videos = self.page.locator("button.tw-link")
        count = streaming_videos.count()
        # Here the documentation is not that clear - click on any video
        # There are many ways to solve this
        streaming_videos_list = [streaming_videos.nth(i) for i in range(count)]
        choosen_streaming_video = streaming_videos_list[count-1]
        choosen_streaming_video.click()
        screenshot_name = self.page.url.strip().split("/")[-1]
        self.wait_for_fully_loaded_stream()
        self.take_screenshot(screenshot_name + ".png")
