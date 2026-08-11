from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.recipes import recipe_router

from database import create_engine
from sqlmodel import SQLModel
import models

app = FastAPI()

origins = [
	"http://localhost:5173"
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.on_event("startup")
def create_tables():
	

app.include_router(recipe_router)

