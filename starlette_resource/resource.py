import asyncio
import typing

from starlette.concurrency import run_in_threadpool
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response, PlainTextResponse
from starlette.types import Scope, Receive, Send


class Resource:
    scope: typing.Optional[Scope] = None
    receive: typing.Optional[Receive] = None
    send: typing.Optional[Send] = None

    def __call__(self, scope: Scope, receive: Receive, send: Send) -> 'Resource':
        assert scope["type"] == "http"
        self.scope = scope
        self.receive = receive
        self.send = send

        return self

    def __await__(self) -> typing.Generator:
        return self.dispatch().__await__()

    async def dispatch(self) -> None:
        request = Request(self.scope, receive=self.receive)
        handler_name = "get" if request.method == "HEAD" else request.method.lower()
        handler = getattr(self, handler_name, self.method_not_allowed)
        is_async = asyncio.iscoroutinefunction(handler)

        if is_async:
            response = await handler(request)
        else:
            response = await run_in_threadpool(handler, request)

        await response(self.scope, self.receive, self.send)

    async def method_not_allowed(self, _: Request) -> Response:
        # If we're running inside a starlette application then raise an
        # exception, so that the configurable exception handler can deal with
        # returning the response. For plain ASGI apps, just return the response.
        if "app" in self.scope:
            raise HTTPException(status_code=405)

        return PlainTextResponse("Method Not Allowed", status_code=405)
