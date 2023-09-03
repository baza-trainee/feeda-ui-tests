import pytest
import os
import time
import configparser
from playwright.sync_api import sync_playwright, Playwright, Page
from pages.login_page import LoginPage
from pages.add_and_change_participants_page import AddAndChangeParticipantPage
from pages.participant_page import ParticipantPage


@pytest.fixture(scope="session")
def config():
    config_file_path = os.path.join("../config", "config.ini")
    config_parser = configparser.ConfigParser(os.environ)
    config_parser.read(config_file_path)

    ui_config = {
        "base_url": config_parser.get("ui", "base_url"),
        "username": config_parser.get("ui", "username"),
        "password": config_parser.get("ui", "password"),
    }

    yield ui_config


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser_context(get_playwright):
    with get_playwright.chromium.launch(headless=False) as browser:
        context = browser.new_context()
        yield context


@pytest.fixture
def login_page(browser_context, config):
    page = browser_context.new_page()
    login_page = LoginPage(page=page)
    yield login_page


@pytest.fixture
def login(config, browser_context):
    page = browser_context.new_page()
    page.goto(config.get('base_url') + '/login')
    page.locator('//*[@id="login"]').fill(config.get('username'))
    page.locator('//*[@id="password"]').fill(config.get('password'))
    page.locator('//*[@id="box"]').click()
    page.locator('//html/body/div/div/form/button').click()
    yield page


@pytest.fixture
def add_participants_page(config, login):
    page = login
    page.goto(config.get('base_url')+'/participants/create')
    add_participants_page = AddAndChangeParticipantPage(page=page)
    yield add_participants_page


@pytest.fixture
def change_participants_page(config, login):
    page = login
    id = "026b1fc3-a089-4788-8bf6-7833343e4197"
    page.wait_for_timeout(5000)
    page.goto(config.get('base_url')+f'/participants/edit/{id}')
    change_participants_page = AddAndChangeParticipantPage(page=page)
    yield change_participants_page


@pytest.fixture
def participant_page(config, login):
    page = login
    page.goto(config.get('base_url')+f'/participants')
    participants_page = ParticipantPage(page=page)
    yield participants_page


# @pytest.fixture
# def participant(config, add_participants_page):
#     add_participants_page.enter_first_name(firs_name=first_name)
#     add_participants_page.enter_last_name(last_name=last_name)
#     add_participants_page.enter_stack(stack=stack)
#     # Дропдауни
#     add_participants_page.enter_city(city=city)
#     add_participants_page.enter_comment(comment=comment)
#     add_participants_page.enter_discord(discord=discord)
#     add_participants_page.enter_linkedin(linkedin=linkedIn)
#     add_participants_page.enter_phone_number(phone_number=phone_number)
#     add_participants_page.enter_email(email=email)
#     add_participants_page.click_button_save_changes()
#     yield

