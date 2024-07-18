from fastapi import APIRouter, Depends, HTTPException
from models.note import NoteCreate, NoteUpdate
from database import note_collection

router = APIRouter()

@router.post("/notes")
async def create_note(note: NoteCreate):
    note_data = note.dict()
    await note_collection.insert_one(note_data)
    return {"msg": "Note created successfully"}

@router.get("/notes")
async def get_notes():
    notes = await note_collection.find().to_list(1000)
    return notes

@router.put("/notes/{note_id}")
async def update_note(note_id: str, note: NoteUpdate):
    await note_collection.update_one({"_id": note_id}, {"$set": note.dict()})
    return {"msg": "Note updated successfully"}

@router.delete("/notes/{note_id}")
async def delete_note(note_id: str):
    await note_collection.delete_one({"_id": note_id})
    return {"msg": "Note deleted successfully"}
