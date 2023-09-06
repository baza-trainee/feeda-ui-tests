import pytest
from assertpy import assert_that, soft_assertions


class TestParticipantPage:
    def test_add_participant_button(self, participant_page):
        participant_page.click_add_participant()
        participant_page.click_add_participant()
        participant_page.page.wait_for_url("http://localhost:3000/participants/create")
        with soft_assertions():
            assert_that(participant_page.page.url).is_equal_to("http://localhost:3000/participants/create")


    def test_change_participant_button(self, participant_page):
        participant_page.click_change_participant()
        participant_page.click_change_participant()
        participant_page.page.wait_for_timeout(3000)
        with soft_assertions():
            assert_that(participant_page.page.url).contains('http://localhost:3000/participants/edit/')

    def test_delete_partcipant_button(self, participant_page):
        participant_page.page.wait_for_timeout(5000)
        participant_page.enter_search_field(text='іваріварівр')
        participant_page.enter_search_field(text='іваріварів')
        participant_page.click_button_search()
        participant_page.click_delete_participant()
        participant_page.click_approve_delete()
        participant_page.enter_search_field(text='іваріварівр')
        participant_page.enter_search_field(text='іваріварів')
        participant_page.click_button_search()
        res = participant_page.dont_find_text()
        assert res == 'Нічого не знайдено'


    def test_open_card_participant(self, participant_page):
        participant_page.click_card_participant()
        participant_page.click_card_participant()
        participant_page.page.wait_for_timeout(3000)
        with soft_assertions():
            assert_that(participant_page.page.url).contains('http://localhost:3000/participants/')