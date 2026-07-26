from fastapi import APIRouter,HTTPException
from schemas.recipe import CreateRecipe,Recipe

recipe_router = APIRouter()

recipes = []
recipeID = 0

@recipe_router.get("/")
async def get_recipes():
	return recipes

@recipe_router.post("/recipe", response_model=Recipe)
async def add_recipe(recipe:CreateRecipe):
	global recipeID 

	new_recipe = Recipe(
		id = recipeID,
		name = recipe.name,
		description = recipe.description,
		ingredients = recipe.ingredients,
		instructions = recipe.instructions,
		prep_time = recipe.prep_time,
		cook_time = recipe.cook_time,
		servings = recipe.servings,
		difficulty = recipe.difficulty
	)

	recipes.append(new_recipe)
	recipeID += 1

	return new_recipe

@recipe_router.delete("/recipe{id}")
async def delete_recipe(id: int):
	for recipe in recipes:
		if recipe.id == id:
			recipes.remove(recipe)
			return {"Message:","Recipe Deleted Successfully"}
	
	raise HTTPException(
		status_code = 404,
		detail = "Recipe Not Found"
	)

@recipe_router.patch("/recipe{id}")
async def update_recipe():
	return "Updated recipe"