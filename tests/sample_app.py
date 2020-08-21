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
