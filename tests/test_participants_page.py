import time
import pytest
from assertpy import assert_that, soft_assertions


class TestParticipantPage:
    def test_add_participant_button(self, participant_page):
        participant_page.click_add_participant()
        participant_page.click_add_participant()
        participant_page.page.wait_for_url("http://localhost:3000/participants/create")
        with soft_assertions():
            assert_that(participant_page.page.url).is_equal_to("http://localhost:3000/participants/create")

