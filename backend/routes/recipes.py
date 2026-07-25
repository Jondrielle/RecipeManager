from fastapi import APIRouter

recipe_router = APIRouter()

recipes = []

@recipe_router.get("/")
async def get_recipes():
	return {"recipes"}

@recipe_router.post("/recipe")
async def add_recipe():
	return "Created recipe"

@recipe_router.delete("/recipe")
async def delete_recipe():
	return "Delete recipe"

@recipe_router.patch("/recipe{id}")
async def update_recipe():
	return "Updated recipe"