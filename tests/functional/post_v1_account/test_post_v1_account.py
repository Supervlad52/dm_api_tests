from collections import namedtuple
from datetime import datetime
from json import loads

import pytest

from helpers.account_helper import AccountHelper
from restclient.configuration import Configuration as MaihogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration
from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True,
            # sort_keys=True
        )
    ]
)


@pytest.fixture
def mailhog_api():
    mailhog_configuration = MaihogConfiguration(host='http://5.63.153.31:5025')
    mailhog_client = MailHogApi(configuration=mailhog_configuration)
    return mailhog_client


@pytest.fixture
def account_api():
    dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)
    account = DMApiAccount(configuration=dm_api_configuration)
    return account


@pytest.fixture
def account_helper(
        account_api,
        mailhog_api
):
    account_helper = AccountHelper(mailhog=mailhog_api, dm_account_api=account_api)
    return account_helper


@pytest.fixture()
def prapare_user():
    now = datetime.now()
    data = now.strftime("%d_%m_%Y_%H_%M_%S")
    login = f'pestov_test_{data}'
    email = f'{login}@mail.ru'
    password = '123456789'
    User = namedtuple("User", ["login", "password", "email"])
    user = User(login=login, password=password, email=email)
    return user


def test_post_v1_account(
        account_helper,
        prapare_user
):
    login = prapare_user.login
    password = prapare_user.password
    email = prapare_user.email
    account_helper.register_new_user(login=login, password=password, email=email)
    account_helper.user_login(login=login, password=password)
