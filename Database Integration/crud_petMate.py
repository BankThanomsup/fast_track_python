from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
from pathlib import Path
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# ----------------- Load .env -----------------
ENV_FILE = Path(__file__).parent / ".env"
load_dotenv(ENV_FILE)

MONGO_URI = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("DATABASE_NAME", "petmate")

if not MONGO_URI:
    raise RuntimeError("MONGODB_URL is not set in .env")

# ----------------- MongoDB Setup -----------------
client = MongoClient(MONGO_URI, server_api=ServerApi("1"))
db = client[DB_NAME]
collection = db["pets"]

# ----------------- FastAPI Setup -----------------
app = FastAPI(title="PetMate CRUD API")

# ----------------- Pydantic Models -----------------
class Pet(BaseModel):
    name: str
    type: str
    age: int

class PetOut(Pet):
    _id: str

# ----------------- CRUD Endpoints -----------------

# Create
@app.post("/pets", response_model=PetOut)
def create_pet(pet: Pet):
    if collection.find_one({"name": pet.name}):
        raise HTTPException(status_code=400, detail="Pet already exists")
    result = collection.insert_one(pet.model_dump())
    pet_data = pet.model_dump()
    pet_data["_id"] = str(result.inserted_id)
    return pet_data

# Read all
@app.get("/pets", response_model=List[PetOut])
def get_all_pets():
    pets = []
    for doc in collection.find({}, {"_id": 1, "name": 1, "type": 1, "age": 1}):
        doc["_id"] = str(doc["_id"])  # แปลง ObjectId → str
        pets.append(doc)
    return pets

# Read by name
@app.get("/pets/{name}", response_model=PetOut)
def get_pet(name: str):
    doc = collection.find_one({"name": name})
    if not doc:
        raise HTTPException(status_code=404, detail="Pet not found")
    doc["_id"] = str(doc["_id"])
    return doc

# Update
@app.put("/pets/{name}", response_model=PetOut)
def update_pet(name: str, updates: Pet):
    result = collection.update_one({"name": name}, {"$set": updates.model_dump()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Pet not found")
    doc = collection.find_one({"name": name})
    doc["_id"] = str(doc["_id"])
    return doc

# Delete
@app.delete("/pets/{name}", response_model=dict)
def delete_pet(name: str):
    result = collection.delete_one({"name": name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"deleted_count": result.deleted_count}
