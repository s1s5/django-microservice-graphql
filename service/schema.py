import strawberry


@strawberry.type
class Query:
    @strawberry.field
    async def hello(self) -> str:
        return "hello world"


schema = strawberry.Schema(
    query=Query,
)
