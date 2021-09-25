from json import loads

from ..exceptions import AshyqException, RetryException


class BaseSession:
    headers: dict

    def request(self, *args, **kwargs):
        ...


class BaseDriver:
    _session: BaseSession
    main: ...

    def check_result(self, status_code: int, text: str) -> dict:
        if status_code == 401:
            self.main.refresh()
            raise RetryException

        json = loads(text)

        if 'Errors' in json:
            raise AshyqException

        if 'access_token' in json:
            self.main.access_token = json['access_token']
        if 'refresh_token' in json:
            self.main.refresh_token = json['refresh_token']

        return json

    def request(self, *args, **kwargs) -> dict:
        ...

    def open(self):
        ...

    def close(self):
        ...
