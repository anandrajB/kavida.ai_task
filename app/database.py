from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

app = FastAPI()


client = AsyncIOMotorClient("mongodb+srv://venzo:root@chat-app.b6llhui.mongodb.net/")

db = client["chat-app"]
