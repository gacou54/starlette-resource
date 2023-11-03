# Starlette-resource
[![ci](https://github.com/gacou54/starlette-resource/workflows/Test/badge.svg)](https://github.com/gacou54/starlette-resource/actions?query=workflow%3ATest)

[Starlette](https://www.starlette.io/) resource classes that helps you follow a layered architecture.

This module was made to facilitate the implementation of a layered architecture.
The `Resource` and` WebSocketResource` classes are essentially the same things as Starlette's
[`HTTPEndpoint`](https://www.starlette.io/endpoints/#httpendpoint) and [`WebSocketEndpoint`](https://www.starlette.io/endpoints/#websocketendpoint)
classes. So you can use these classes in the same way.

The difference is that the `Resource` and `WebSockerResource` must be instantiated before being passed to Starlette's [`Route`](https://www.starlette.io/routing/).

Works with Python 3.8+.

### Example
```python
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket

from starlette_resource import Resource, WebSocketResource


class GreetingService:
    async def greet(self, name: str) -> str:
        return f'Hello {name}!'


class GreetingResource(Resource):
    def __init__(self, hello_service: GreetingService) -> None:
        self.hello_service = hello_service

    async def get(self, req: Request) -> PlainTextResponse:
        name = req.path_params['name']
        greeting_message = await self.hello_service.greet(name)

        return PlainTextResponse(greeting_message)
    
    async def post(self, req: Request):
        ...

    async def put(self, req: Request):
        ...

    async def delete(self, req: Request):
        ...


class GreetingWebSocketResource(WebSocketResource):
    def __init__(self, hello_service: GreetingService) -> None:
        self.hello_service = hello_service

    async def on_receive(self, websocket: WebSocket, data: str) -> None:
        greeting_message = await self.hello_service.greet(data)

        await websocket.send_text(greeting_message)


# Services
greeting_service = GreetingService()

# Resources
greeting_resource = GreetingResource(greeting_service)
greeting_websocket_resource = GreetingWebSocketResource(greeting_service)

app = Starlette(
    debug=True,
    routes=[
        Route('/greet/{name}', greeting_resource),
        WebSocketRoute('/websocket_greet', greeting_websocket_resource)
    ]
)
```

### Installation

Simply install from PyPI:

`pip install starlette-resource`