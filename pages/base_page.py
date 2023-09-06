from playwright.sync_api import Page, Locator
from locators.base_locators import BaseLocators


class BasePage:
    locators = BaseLocators
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

    def enter_search_field(self, text):
        self.page.wait_for_selector(self.locators.SEARCH_FIELD).fill(text)

    def click_button_search(self):
        self.page.wait_for_selector(self.locators.BUTTON_SEARCH).click()

    def dont_find_text(self):
        return self.find_element(self.locators.DONT_FIND).text_content()
