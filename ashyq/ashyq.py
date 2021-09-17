from requests import Session, Response
from base64 import b64encode
from utils import random_string

from exceptions import AshyqException, RetryException

from typing import Optional, Union


class URL:
    new_install = 'https://ashyq.curs.kz/ashyq/v2/api/otp/newInstall'
    connect = 'https://ashyq.curs.kz/ashyq/identity/connect/token'
    user = 'https://ashyq.curs.kz/ashyq/v2/api/user'
    qrpass = 'https://ashyq.curs.kz/ashyq/v2/api/qrpass/check'
    employee_check = 'https://ashyq.curs.kz/ashyq/v2/api/qrpass/employee/check'


class Ashyq:
    def __init__(self, phone_number: str, device_id: Optional[str]=random_string(16)):
        self.phone_number: str = phone_number

        self.access_token: str = None
        self.refresh_token: str = None

        self.auth_token: str = 'Basic {}'.format(
            b64encode(
                bytes('ad3c48bd01f571d9cf74916aec79a619c991659f1129e2f2e31734bb8927f08e407d7eab', 'utf-8')
            )
        )

        self.device_id: str = device_id

        self._session: Session = Session()

    def _check_result(self, response: Response) -> Union[Exception, dict]:
        if response.status_code == 401:
            self.refresh()
            raise RetryException

        json = response.json()

        if 'Errors' in json:
            raise AshyqException

        if 'access_token' in json:
            self.access_token = json['access_token']
        if 'refresh_token' in json:
            self.refresh_token = json['refresh_token']

        self.auth_token = 'Bearer {}'.format(self.access_token)

        return json

    def _request(self, url: str, data: Optional[dict]=None, headers: Optional[dict]=None, json: Optional[dict]=None, method: str='GET') -> dict:
        try:
            return self._check_result(
                self._session.request(
                    method, url, data=data, headers=headers, json=json
                )
            )

        except RetryException:
            return self._check_result(
                self._session.request(
                    method, url, data=data, headers=headers, json=json
                )
            )

    def new_install(self) -> dict:
        return self._request(
            URL.new_install, json={
                'deviceId': self.device_id,
                'noSms': False,
                'phoneNumber': self.phone_number
            }, method='POST'
        )

    def refresh(self) -> dict:
        return self._request(
            URL.connect, data={
                'username': self.phone_number,
                'refresh_token': self.refresh_token,
                'scope': 'api offline_access',
                'acr_values': 'DeviceId={}&LoginType=PhoneNumber&'.format(self.device_id),
                'grant_type': 'refresh_token'
            }, headers={
                'Authorization': self.auth_token
            }, method='POST'
        )

    def connect(self, code: Union[int, str]) -> dict:
        return self._request(
            URL.connect, data={
                'username': self.phone_number,
                'password': code,
                'scope': 'api offline_access',
                'acr_values': 'DeviceId={}&LoginType=PhoneNumber&'.format(self.device_id),
                'grant_type': 'password'
            }, headers={
                'Authorization': self.auth_token
            }, method='POST'
        )

    def get_user(self) -> dict:
        return self._request(
            URL.user, headers={
                'Authorization': self.auth_token
            }, method='GET'
        )

    @property
    def user(self) -> dict:
        if not hasattr(self, '_user'):
            setattr(self, '_user', self.get_user())

        return getattr(self, '_user')

    def user_pcr(self) -> dict:
        return self._request(
            URL.qrpass, json={
                'BIN': '000000000012',
                'BuildingRKA': '0011',
                'Code': 'android',
                'Lang': 'ru',
                'OfficeRKA': '1',
                'Type': 'entry'
            }, headers={
                'Authorization': self.auth_token
            }, method='POST'
        )

    def pcr(self, iin: str) -> dict:
        return self._request(
            URL.employee_check, json={
                'IIN': iin,
                'Lang': 'ru',
                'Type': 'entry'
            }, headers={
                'Authorization': self.auth_token
            }, method='POST'
        )
