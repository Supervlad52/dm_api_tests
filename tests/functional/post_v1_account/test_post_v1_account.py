def test_post_v1_account(
        account_helper,
        prapare_user
):
    login = prapare_user.login
    password = prapare_user.password
    email = prapare_user.email
    account_helper.register_new_user(login=login, password=password, email=email)
    account_helper.user_login(login=login, password=password)
