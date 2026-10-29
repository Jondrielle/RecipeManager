from database import create_db_and_tables
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.recipes import recipe_router

app = FastAPI()

origins = [
	"http://localhost:5173",
	"https://recipemanaging.netlify.app"
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    

app.include_router(recipe_router)

