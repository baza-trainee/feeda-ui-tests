import pytest
from assertpy import assert_that, soft_assertions


class TestAddParticipants:
    @pytest.mark.parametrize("first_name, last_name, stack, city, comment, discord,"
                             " linkedIn, phone_number, email", [
                                 pytest.param(
                                     'John',
                                     'Test',
                                     'Python, Allure, Postman',
                                     'Test',
                                     'Test comment',
                                     'john#0000',
                                     'https://www.linkedin.com/feed/',
                                     '+380123456789',
                                     'john123@gmail.com',
                                     id="add_with_valid_data"
                                 )
                             ])
    def test_add_success(self, add_participants_page, first_name, last_name, stack, city, comment, discord,
                         linkedIn, phone_number, email):
        add_participants_page.enter_first_name(firs_name=first_name)
        add_participants_page.enter_last_name(last_name=last_name)
        add_participants_page.enter_stack(stack=stack)
        # Дропдауни
        add_participants_page.enter_city(city=city)
        add_participants_page.enter_comment(comment=comment)
        add_participants_page.enter_discord(discord=discord)
        add_participants_page.enter_linkedin(linkedin=linkedIn)
        add_participants_page.enter_phone_number(phone_number=phone_number)
        add_participants_page.enter_email(email=email)
        add_participants_page.click_button_save_changes()
        # res = add_participants_page.find_element('Ваші дані було успішно збережено.')
        # with soft_assertions():
        #     assert_that(res).is_equal_to("Ваші дані було успішно збережено.")
