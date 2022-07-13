from fastapi import APIRouter, status, HTTPException, Depends

# from server import models
# from server.schemas import book, user
# from server.database import get_db
# from sqlalchemy.orm import Session
# from typing import List


router = APIRouter(
    prefix ="/user",
    tags = ['Users'] 
)

@router.get('/test')
def get_test():
    return 'test'