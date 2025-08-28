import allure

from checkers.post_v1_account import PostV1Account


@allure.suite('Тесты на проверку метода POST v1/account')
@allure.sub_suite('Позитивные тесты')
class TestsPostV1Account:
    @allure.title('Проверка регистрации нового пользователя')
    def test_post_v1_account(
            self,
            account_helper,
            prapare_user
    ):
        login = prapare_user.login
        password = prapare_user.password
        email = prapare_user.email

        account_helper.register_new_user(login=login, password=password, email=email)
        response = account_helper.user_login(login=login, password=password, validate_response=True)
        PostV1Account.check_response_values(response)
