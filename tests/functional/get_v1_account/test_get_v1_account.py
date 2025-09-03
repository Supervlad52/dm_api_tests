from checkers.http_checkers import check_status_code_http


def test_get_v1_account_auth(auth_account_helper):
    with check_status_code_http(200):
        auth_account_helper.dm_account_api.account_api.get_v1_account()
    # response = auth_account_helper.dm_account_api.account_api.get_v1_account()
    # with soft_assertions():
    #     assert_that(response.resource.login).is_equal_to('pestov_test')
    #     assert_that(response.resource.online).is_equal_to(datetime)
    #     assert_that(response.resource.roles).contains(UserRole.GUEST, UserRole.PLAYER)


def test_get_v1_account_no_auth(account_helper):
    with check_status_code_http(401, 'User must be authenticated'):
        account_helper.dm_account_api.account_api.get_v1_account()