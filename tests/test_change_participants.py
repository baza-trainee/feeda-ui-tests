import time

import pytest
from assertpy import assert_that, soft_assertions


class TestChangeParticipants:
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
    def test_change_participant_success(self, change_participants_page, first_name, last_name, stack, city, comment,
                                        discord, linkedIn, phone_number, email):
        change_participants_page.enter_first_name(firs_name=first_name)
        change_participants_page.enter_last_name(last_name=last_name)
        change_participants_page.enter_stack(stack=stack)
        # Дропдауни
        change_participants_page.enter_city(city=city)
        change_participants_page.enter_comment(comment=comment)
        change_participants_page.enter_discord(discord=discord)
        change_participants_page.enter_linkedin(linkedin=linkedIn)
        time.sleep(10)
        change_participants_page.enter_phone_number(phone_number=phone_number)
        change_participants_page.enter_email(email=email)
        change_participants_page.click_button_save_changes()
        # res = add_participants_page.find_element('Ваші дані було успішно збережено.')
        # with soft_assertions():
        #     assert_that(res).is_equal_to("Ваші дані було успішно збережено.")
