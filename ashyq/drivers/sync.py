from requests import Session, Response

from .base import BaseDriver
from ..exceptions import RetryException

from typing import Optional


class SyncDriver(BaseDriver):
    def __init__(self):
        self._session = Session()

    def request(self, url: str, data: Optional[dict]=None, headers: Optional[dict]=None, json: Optional[dict]=None, method: str='GET') -> dict:
        try:
            request: Response = self._session.request(
                method  = method,
                url     = url,
                data    = data,
                headers = headers,
                json    = json
            )

            return self.check_result(request.status_code, request.text)

        except RetryException:
            request: Response = self._session.request(
                method  = method,
                url     = url,
                data    = data,
                headers = headers,
                json    = json
            )

            return self.check_result(request.status_code, request.text)
