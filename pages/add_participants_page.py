from pages.base_page import BasePage
from locators.add_participant_locators import AddParticipantLocators


class AddParticipantPage(BasePage):
    locator = AddParticipantLocators

    # def enter_first_name(self, firs_name: str):
    #     firs_name_input = self.find_element(locator=self.locator.FIRSTNAME)
    #     firs_name_input.click()
    #     firs_name_input.fill(firs_name)

    def enter_first_name(self, firs_name: str):
        self.fill_element(locator=self.locator.FIRSTNAME, text=firs_name)

    # def enter_last_name(self, last_name: str):
    #     firs_name_input = self.find_element(locator=self.locator.LASTNAME)
    #     firs_name_input.click()
    #     firs_name_input.fill(last_name)

    def enter_last_name(self, last_name: str):
        self.fill_element(locator=self.locator.LASTNAME, text=last_name)

    # def enter_stack(self, stack: str):
    #     firs_name_input = self.find_element(locator=self.locator.STACK)
    #     firs_name_input.click()
    #     firs_name_input.fill(stack)

    def enter_stack(self, stack: str):
        self.fill_element(locator=self.locator.STACK, text=stack)

    def click_list_speciality(self):
        login_button = self.find_element(locator=self.locator.LIST_SPECIALITY)
        login_button.click()


    # def enter_city(self, city: str):
    #     firs_name_input = self.find_element(locator=self.locator.CITY)
    #     firs_name_input.click()
    #     firs_name_input.fill(city)


    def enter_city(self, city: str):
        self.fill_element(locator=self.locator.CITY, text=city)

    # def enter_comment(self, comment: str):
    #     firs_name_input = self.find_element(locator=self.locator.COMMENT)
    #     firs_name_input.click()
    #     firs_name_input.fill(comment)

    def enter_comment(self, comment: str):
        self.fill_element(locator=self.locator.COMMENT, text=comment)

    def click_send_letter(self):
        self.click_element(locator=self.locator.BUTTON_SEND_LETTER)

    # def enter_discord(self, discord: str):
    #     firs_name_input = self.find_element(locator=self.locator.DISCORD)
    #     firs_name_input.click()
    #     firs_name_input.fill(discord)

    def enter_discord(self, discord: str):
        self.fill_element(locator=self.locator.DISCORD, text=discord)

    def enter_linkedin(self, linkedin: str):
        self.fill_element(locator=self.locator.LINKEDIN, text=linkedin)

    def enter_phone_number(self, phone_number: str):
        self.fill_element(locator=self.locator.PHONE_NUMBER, text=phone_number)

    def enter_email(self, email: str):
        self.fill_element(locator=self.locator.EMAIL, text=email)

    def click_button_add_project(self):
        self.click_element(locator=self.locator.BUTTON_ADD_PROJECT)

    def click_button_save_changes(self):
        self.click_element(locator=self.locator.BUTTON_SAVE_CHANGES)

    def click_button_dont_save_changes(self):
        self.click_element(locator=self.locator.BUTTON_DONT_SAVE_CHANGES)

    def click_button_list_project(self):
        self.click_element(locator=self.locator.BUTTON_LIST_PROJECT)

    def click_button_delete_project(self):
        self.click_element(locator=self.locator.BUTTON_DELETE_PROJECT)

