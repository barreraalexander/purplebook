from fastapi import APIRouter, status, HTTPException, Depends

router = APIRouter(
    prefix ="/gql",
    tags = ['Graph QL'] 
)
