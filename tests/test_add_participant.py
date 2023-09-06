import time

import pytest
from assertpy import assert_that, soft_assertions
# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# def test_run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("http://localhost:3000/login")
#     page.goto("http://localhost:3000/participants")
#     page.goto("http://localhost:3000/login")
#     page.get_by_placeholder("Логін").click()
#     page.get_by_placeholder("Логін").fill("admin123@gmail.com")
#     page.get_by_placeholder("Пароль").click()
#     page.get_by_placeholder("Пароль").fill("Feeda12345")
#     page.locator("#box").click()
#     page.get_by_role("button", name="Увійти").click()
#     page.get_by_role("link", name="Додати учасника").click()
#     page.get_by_placeholder("Ім'я").click()
#     page.get_by_placeholder("Ім'я").fill("SFdsf")
#     page.get_by_placeholder("Прізвище").click()
#     page.get_by_placeholder("Прізвище").fill("FSdfs")
#     page.get_by_placeholder("HTML,CSS,TS,Node").click()
#     page.get_by_placeholder("HTML,CSS,TS,Node").fill("sdfsdfsdfsd")
#     page.locator("label").filter(has_text="РольNone").locator("svg").click()
#     page.locator("#react-select-speciality-option-2").click()
#     time.sleep(5)
#     page.locator("label").filter(has_text="Досвід *Так/Ні").locator("svg").click()
#     page.locator("#react-select-experience-option-0").click()
#     time.sleep(5)
#     page.locator("label").filter(has_text="Тип участі *Платний").locator("svg").click()
#     page.locator("#react-select-type_participant-option-1").click()
#     page.get_by_placeholder("Країна").click()
#     page.get_by_placeholder("Країна").fill("Vdsad")
#     page.get_by_placeholder("XXXX#XXXX").click()
#     page.get_by_placeholder("XXXX#XXXX").fill("kozlov2777")
#     page.get_by_placeholder("+XXXXXXXXXXXX").click()
#     page.get_by_placeholder("+XXXXXXXXXXXX").fill("+380955578729")
#     page.get_by_placeholder("xxx@xxxx.xxx").click()
#     page.get_by_placeholder("xxx@xxxx.xxx").fill("kozlov2777@gmail.com")
#     page.get_by_placeholder("www.linkedin.com/in/").click()
#     page.get_by_placeholder("www.linkedin.com/in/").fill("https://www.linkedin.com/in/oleksandr-kozlov-a74889256/")
#     page.get_by_role("button", name="Зберегти зміни").click()
#     page.get_by_placeholder("XXXX#XXXX").click()
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     test_run(playwright)



class TestAddParticipants:
    @pytest.mark.parametrize("first_name, last_name, stack, city, comment, discord,"
                             " linkedIn, phone_number, email", [
                                 pytest.param(
                                     'Johnz',
                                     'Test',
                                     'Python, Allure, Postman, Selenium',
                                     'Test',
                                     'Test comment',
                                     'john6789',
                                     'https://www.linkedin.com/in/oleksandr-kozlov-a74889256/',
                                     '+380955578729',
                                     'john123@gmail.com',
                                     id="add_with_valid_data"
                                 )
                             ])
    def test_add_success(self, add_participants_page, first_name, last_name, stack, city, comment, discord,
                         linkedIn, phone_number, email):
        add_participants_page.enter_first_name(firs_name=first_name)
        add_participants_page.enter_last_name(last_name=last_name)
        add_participants_page.enter_stack(stack=stack)
        add_participants_page.click_list_speciality()
        add_participants_page.click_qa()
        add_participants_page.click_list_experience()
        add_participants_page.click_experience_true()
        add_participants_page.click_list_type_participant()
        add_participants_page.click_type_participant_free()
        add_participants_page.enter_city(city=city)
        add_participants_page.enter_comment(comment=comment)
        add_participants_page.enter_discord(discord=discord)
        add_participants_page.enter_linkedin(linkedin=linkedIn)
        add_participants_page.enter_phone_number(phone_number=phone_number)
        add_participants_page.enter_email(email=email)
        add_participants_page.click_button_save_changes()
        res = add_participants_page.page.wait_for_selector('//html/body/div/div[2]/div/div/p[2]')
        res_text = res.text_content()
        assert res_text == 'Ваші дані було успішно збережено.'
