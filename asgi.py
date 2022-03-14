import os
from typing import List

import django
from django.conf import settings
from starlette.applications import Starlette
from starlette.middleware import Middleware
from strawberry import Schema
from strawberry.asgi import GraphQL
from strawberry.utils.importer import import_module_symbol

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

django.setup(set_prefix=False)

middlewares: List[Middleware] = []

schema = import_module_symbol("service.schema:schema")
if not isinstance(schema, Schema):
    raise Exception("schema must be instance of strawberry.Schema")

app = Starlette(debug=settings.DEBUG, middleware=middlewares)
graphql_app = GraphQL(
    schema=schema,
    graphiql=settings.DEBUG,
    debug=settings.DEBUG,
    keep_alive=False,
    keep_alive_interval=10,
)

app.add_route("/", graphql_app)
app.add_websocket_route("/", graphql_app)
