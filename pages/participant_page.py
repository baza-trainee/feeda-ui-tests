from pages.base_page import BasePage
from locators.participants_locators import ParticipantsLocators


class ParticipantPage(BasePage):
    locator = ParticipantsLocators

    def click_add_participant(self):
        self.page.locator(self.locator.BUTTON_ADD_PARTICIPANT).click()

    def click_card_participant(self):
        self.page.locator(self.locator.CARD).click()

    def click_delete_participant(self):
        self.page.locator(self.locator.DELETE_PARTICIPANT).click()

    def click_change_participant(self):
        self.page.locator(self.locator.CHANGE_PARTICIPANT).click()

    def click_approve_delete(self):
        self.click_element(locator=self.locator.APPROVE_DELETE)