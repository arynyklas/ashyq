from . import types
from .drivers.base import BaseDriver
from .utils import random_string, to_object

from base64 import b64encode

from typing import Optional, Union


class Ashyq:
    _user: types.User = None

    def _access_token_getter(self):
        return self._access_token

    def _access_token_setter(self, val: str):
        self._access_token = val
        self._driver._session.headers['Authorization'] = 'Bearer {}'.format(self.access_token)
        self.logged_on = True

    access_token = property(_access_token_getter, _access_token_setter)

    def __init__(self, driver: BaseDriver, phone_number: str, device_id: str=random_string(16), access_token: str=None, refresh_token: str=None):
        """
        Base Ashyq class
        """
        self._driver: BaseDriver = driver
        self._driver.main = self

        self.phone_number: str = phone_number

        self.access_token: str = access_token
        self.refresh_token: str = refresh_token

        self.logged_on: bool = False

        self.device_id: str = device_id

        self._driver._session.headers['Authorization'] = b64encode(
            bytes('ad3c48bd01f571d9cf74916aec79a619c991659f1129e2f2e31734bb8927f08e407d7eab', 'utf-8')
        ).decode()

        self._driver.open()

    def _request(self, url: str, data: Optional[dict]=None, headers: Optional[dict]=None, json: Optional[dict]=None, method: str='GET') -> dict:
        return self._driver.request(
            url     = url,
            data    = data,
            headers = headers,
            json    = json,
            method  = method
        )

    def new_install(self) -> types.Code:
        """Sends an SMS code to log in to your account.

        :return: On success, a server response is returned
        :rtype: :obj:`types.Code`
        """
        return to_object(self._request(
            types.URL.new_install, json={
                'deviceId': self.device_id,
                'noSms': False,
                'phoneNumber': self.phone_number
            }, method='POST'
        ), types.Code, snake=True)

    def connect(self, code: Union[int, str]) -> types.Connect:
        """Sends a request with an SMS code to access the account.

        :return: On success, login tokens is returned
        :rtype: :obj:`types.Connect`
        """
        return to_object(self._request(
            types.URL.connect, data={
                'username': self.phone_number,
                'password': code,
                'scope': 'api offline_access',
                'acr_values': 'DeviceId={}&LoginType=PhoneNumber&'.format(self.device_id),
                'grant_type': 'password'
            }, method='POST'
        ), types.Connect, snake=True)

    def refresh(self) -> types.Connect:
        """Updates the access token and updates the token for account access.

        :return: On success, updated tokens is returned
        :rtype: :obj:`types.Connect`
        """
        return to_object(self._request(
            types.URL.connect, data={
                'username': self.phone_number,
                'refresh_token': self.refresh_token,
                'scope': 'api offline_access',
                'acr_values': 'DeviceId={}&LoginType=PhoneNumber&'.format(self.device_id),
                'grant_type': 'refresh_token'
            }, method='POST'
        ), types.Connect, snake=True)

    def get_user(self) -> types.User:
        """Gets information about the logged-in user.

        :return: On success, loginned user is returned
        :rtype: :obj:`types.User`
        """
        return to_object(self._request(
            types.URL.user, method='GET'
        ), types.User, snake=False)

    @property
    def user(self) -> types.User:
        """Gets information about the logged-in user.
        Caches user information.

        :return: On success, loginned user is returned
        :rtype: :obj:`types.User`
        """
        if not self._user:
            self._user = self.get_user()

        return self._user

    def user_pcr(self) -> types.Check:
        """Gets information about the PCR of the logged-in user's.

        :return: On success, loginned user user's PCR information is returned
        :rtype: :obj:`types.User`
        """
        return to_object(self._request(
            types.URL.qrpass, json={
                'BIN': '000000000012',
                'BuildingRKA': '0011',
                'Code': 'android',
                'Lang': 'ru',
                'OfficeRKA': '1',
                'Type': 'entry'
            }, method='POST'
        ), types.Check, snake=False)

    def pcr(self, iin: str) -> types.Check:
        """Gets information about the PCR of the any user by his IIN.
        WARNING: works if user is security officer

        :return: On success, user's PCR information is returned
        :rtype: :obj:`types.Check`
        """
        return to_object(self._request(
            types.URL.employee_check, json={
                'IIN': iin,
                'Lang': 'ru',
                'Type': 'entry'
            }, method='POST'
        ), types.Check, snake=False)

    def close(self):
        """
        Closes driver session

        :return:
        """
        self._driver.close()
