from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from database import user_collection
from auth.auth import get_password_hash, create_access_token, verify_password

router = APIRouter()

@router.post("/register")
async def register(user: User):
    user.password = get_password_hash(user.password)
    user_data = user.dict()
    await user_collection.insert_one(user_data)
    return {"msg": "User registered successfully"}

@router.post("/login")
async def login(user: User):
    db_user = await user_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}
