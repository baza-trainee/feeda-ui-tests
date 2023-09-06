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
                                     'john2777',
                                     'https://www.linkedin.com/in/oleksandr-kozlov-a74889256/',
                                     '+380983456789',
                                     'john123@gmail.com',
                                     id="change_with_valid_data"
                                 )
                             ])
    def test_change_participant_success(self, change_participants_page, first_name, last_name, stack, city, comment,
                                        discord, linkedIn, phone_number, email):
        change_participants_page.page.wait_for_timeout(3000)
        change_participants_page.enter_search_field(stack)
        change_participants_page.enter_search_field(stack+' ')
        change_participants_page.click_button_search()
        change_participants_page.page.wait_for_selector('body > div > div > ul > li:nth-child(1) > a > div.css-zvm7fl > button:nth-child(2)').click()
        change_participants_page.enter_first_name(firs_name=first_name)
        change_participants_page.enter_last_name(last_name=last_name)
        change_participants_page.enter_stack(stack=stack)
        change_participants_page.click_list_speciality()
        change_participants_page.click_qa()
        change_participants_page.click_list_experience()
        change_participants_page.click_experience_true()
        change_participants_page.click_list_type_participant()
        change_participants_page.click_type_participant_free()
        change_participants_page.enter_city(city=city)
        change_participants_page.enter_comment(comment=comment)
        change_participants_page.enter_discord(discord=discord)
        change_participants_page.enter_linkedin(linkedin=linkedIn)
        change_participants_page.enter_phone_number(phone_number=phone_number)
        change_participants_page.enter_email(email=email)
        change_participants_page.click_button_save_changes()
        res = change_participants_page.page.wait_for_selector('//html/body/div/div[2]/div/div/p[2]')
        res_text = res.text_content()
        assert res_text == 'Ваші дані було успішно збережено.'
