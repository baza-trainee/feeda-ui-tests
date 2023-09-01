import pytest
from assertpy import assert_that, soft_assertions


class TestLogiPage:
    @pytest.mark.parametrize("url, email, password", [
        pytest.param("http://localhost:3000/login",
                     'qafeeda123@gmail.com',
                     'Baza12345',
                     id="login_with_valid_data"
                     )
    ])
    def test_login_success(self, login_page, url, email, password):
        login_page.navigate_to(url)
        login_page.enter_username(email)
        login_page.enter_password(password)
        login_page.click_login_button()

    @pytest.mark.parametrize("url, email, password", [
        pytest.param("http://localhost:3000/login",
                     'qafe',
                     'Baza12345',
                     id="login_with_invalid_email"
                     )
    ])
    def test_login_username_errors(self, login_page, url, email, password):
        login_page.navigate_to(url)
        login_page.enter_username(email)
        login_page.enter_password(password)
        login_page.click_login_button()
        res = login_page.page.text_content(selector='//html/body/div/div/form/div[2]/div[1]/label[2]')
        with soft_assertions():
            assert_that(res).is_equal_to("Неправильний логін")

    @pytest.mark.parametrize("url, email, password", [
        pytest.param("http://localhost:3000/login",
                     'qafeeda123@gmail.com',
                     'baza12345',
                     id="login_with_invalid_password_lowercase_letter"
                     ),
        pytest.param("http://localhost:3000/login",
                     'qafeeda123@gmail.com',
                     'Baza',
                     id="login_with_invalid_password_without_numbers"
                     )
    ])
    def test_login_password_errors(self, login_page, url, email, password):
        login_page.navigate_to(url)
        login_page.enter_username(email)
        login_page.enter_password(password)
        login_page.click_login_button()
        res = login_page.page.text_content(selector='//html/body/div/div/form/div[2]/div[2]/label[2]')
        with soft_assertions():
            assert_that(res).is_equal_to("Неправильний пароль")
