from fastapi import APIRouter, status, HTTPException, Depends


router = APIRouter(
    prefix ="/users",
    tags = ['Users'] 
)