from starlette.endpoints import WebSocketEndpoint
from starlette.types import Scope, Receive, Send


class WebSocketResource(WebSocketEndpoint):

    def __call__(self, scope: Scope, receive: Receive, send: Send) -> 'WebSocketResource':
        super().__init__(scope, receive, send)

        return self
