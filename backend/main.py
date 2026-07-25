from fastapi import FastAPI
from routes.recipes import recipe_router

app = FastAPI()

app.include_router(recipe_router)

