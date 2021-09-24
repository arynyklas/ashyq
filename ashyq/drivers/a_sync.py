from aiohttp import ClientSession, ClientResponse
from asyncio import get_event_loop, AbstractEventLoop

from .base import BaseDriver
from ..exceptions import RetryException

from typing import Coroutine, Any, Optional


class AsyncDriver(BaseDriver):
    def __init__(self, loop: AbstractEventLoop=get_event_loop()):
        self._session = ClientSession()
        self._loop = loop

    def _process_async(self, corountine: Coroutine) -> Any:
        return self._loop.run_until_complete(corountine)

    def open(self):
        return self._process_async(
            self._session.__aenter__()
        )

    def close(self):
        return self._process_async(
            self._session.__aexit__()
        )

    async def _request(self, url: str, data: Optional[dict]=None, headers: Optional[dict]=None, json: Optional[dict]=None, method: str='GET') -> dict:
        try:
            async with self._session.request(
                method  = method,
                url     = url,
                data    = data,
                json    = json,
                headers = headers
            ) as request:
                request: ClientResponse

                return self.check_result(
                    request.status, await request.text()
                )

        except RetryException:
            async with self._session.request(
                method  = method,
                url     = url,
                data    = data,
                json    = json,
                headers = headers
            ) as request:
                return self.check_result(
                    request.status, await request.text()
                )

    def request(self, *args, **kwargs) -> dict:
        return self._process_async(
            self._request(*args, **kwargs)
        )
