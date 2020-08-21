from starlette.endpoints import HTTPEndpoint
from starlette.types import Scope, Receive, Send


class Resource(HTTPEndpoint):

    def __call__(self, scope: Scope, receive: Receive, send: Send) -> 'Resource':
        super().__init__(scope, receive, send)

        return self
