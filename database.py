# backend/database.py
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb://localhost:27017')
database = client.note_taking_app
user_collection = database.get_collection("users")
note_collection = database.get_collection("notes")
