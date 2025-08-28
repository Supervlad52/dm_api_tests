import allure

from dm_api_account.models.registration import Registration
from dm_api_account.models.user_envelope import UserEnvelope
from restclient.client import RestClient


class AccountApi(RestClient):

    @allure.step('Зарегистрировать нового пользователя')
    def post_v1_account(
            self,
            registration: Registration
    ):
        """Register new user
        :param json_data:
        :return:
        """
        response = self.post(
            path='/v1/account',
            json=registration.model_dump(exclude_none=True, by_alias=True)
        )
        return response

    def get_v1_account(
            self,
            **kwargs
    ):
        """Get current usser
        :return:
        """
        response = self.get(
            path='/v1/account',
            **kwargs
        )
        return response

    @allure.step('Активизировать пользователя')
    def put_v1_account_token(
            self,
            token,
            validate_response=True
    ):
        """
        Activate registered user
        :param token:
        :return:
        """
        headers = {
            'accept': 'text/plain',
        }
        response = self.put(
            path=f'/v1/account/{token}',
            headers=headers
        )
        if validate_response:
            return UserEnvelope(**response.json())
        return response
