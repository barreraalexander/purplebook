import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello User"

    @strawberry.field
    def count(self) -> int:
        return 5

    @strawberry.field
    def myBook(self) -> int:
        return 5


schema = strawberry.Schema(
        Query,
        # config=StrawberryConfig(auto_camel_case=False)
    )

gql = GraphQLRouter(schema)