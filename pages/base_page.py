from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def find_element(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def click_element(self, locator: str):
        element = self.find_element(locator)
        element.click()

    def fill_element(self, locator: str, text: str):
        self.find_element(locator).fill(text)

    def type_text(self, locator: str, text: str):
        element = self.find_element(locator)
        element.type(text)

    def navigate_to(self, url: str):
        self.page.goto(url)
