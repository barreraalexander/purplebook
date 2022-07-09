from fastapi import APIRouter, status, HTTPException, Depends, Request
# from server.routers.strawberry_user import gql as UserSchema

import strawberry
from strawberry.fastapi import GraphQLRouter


router = APIRouter(
    tags = ['Graph QL'] 
)

@router.post('/book_ep')
def book_gql():
    return 'home'

# schema = strawberry.Schema()

