from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    locator = LoginLocators

    def enter_username(self, username: str):
        self.fill_element(locator=self.locator.LOGIN, text=username)

    def enter_password(self, password: str):
        self.fill_element(locator=self.locator.PASSWORD, text=password)

    def click_save_me(self):
        self.page.locator(self.locator.SAVEME).click()

    def click_login_button(self):
        self.find_element(locator=self.locator.LOGIN_BUTTON).click()
