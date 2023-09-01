import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.add_participants_page import AddParticipantPage


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def login_page(get_playwright):
    with get_playwright.chromium.launch() as browser:
        context = browser.new_context()
        page = context.new_page()
        yield LoginPage(page=page)


@pytest.fixture
def add_participants_page(get_playwright):
    with get_playwright.chromium.launch() as browser:
        context = browser.new_context()
        page = context.new_page()
        yield AddParticipantPage(page=page)