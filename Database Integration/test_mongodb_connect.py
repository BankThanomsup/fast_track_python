"""
Minimal example: Load MONGODB_URL from .env, ping MongoDB, 
and create database/collection/document.
"""

from __future__ import annotations
import os
from pathlib import Path
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load .env from the same folder as this script
ENV_FILE = Path(__file__).parent / ".env"
if ENV_FILE.exists():
    load_dotenv(ENV_FILE)
else:
    load_dotenv()  # fallback

# Get MongoDB URI and database name
uri = os.getenv("MONGODB_URL")
db_name = os.getenv("DATABASE_NAME", "petmate")

if not uri:
    raise RuntimeError(
        "MONGODB_URL is not set. Create .env from .env.example and set MONGODB_URL"
    )

# Connect to MongoDB
client = MongoClient(uri, server_api=ServerApi("1"))

# Ping MongoDB
try:
    client.admin.command("ping")
    print("✅ Pinged your deployment. Successfully connected to MongoDB!")
    print(f"   DATABASE_NAME: {db_name}")
except Exception as e:
    raise RuntimeError(f"❌ Connection failed: {e}")

# Create/get database
db = client[db_name]

# Create/get collection
collection = db["pets"]

# Insert a sample document
sample_pet = {"name": "Fluffy", "type": "cat", "age": 2}
insert_result = collection.insert_one(sample_pet)
print(f"Inserted document with _id: {insert_result.inserted_id}")

# Read back documents
print("Current documents in collection 'pets':")
for doc in collection.find():
    print(doc)
