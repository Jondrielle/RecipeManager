from fastapi import APIRouter,HTTPException
from schemas.recipe import CreateRecipe,Recipe,UpdateRecipe

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

@recipe_router.delete("/recipe/{id}")
async def delete_recipe(id:int):
	for recipe in recipes:
		if recipe.id == id:
			recipes.remove(recipe)
			return {"Message:","Recipe Deleted Successfully"}
	
	raise HTTPException(
		status_code = 404,
		detail = "Recipe Not Found"
	)

@recipe_router.patch("/recipes/{id}")
async def update_recipe(id:int, updated_recipe:UpdateRecipe):
	for recipe in recipes:
		if recipe.id == id:
			if updated_recipe.name is not None:
				recipe.name = updated_recipe.name

			if updated_recipe.description is not None:
				recipe.description = updated_recipe.description

			if updated_recipe.ingredients is not None:
				recipe.ingredients = updated_recipe.ingredients

			if updated_recipe.instructions is not None:
				recipe.instructions = updated_recipe.instructions

			if updated_recipe.prep_time is not None:
				recipe.prep_time = updated_recipe.prep_time

			if updated_recipe.cook_time is not None:
				recipe.cook_time = updated_recipe.cook_time

			if updated_recipe.servings is not None:
				recipe.servings = updated_recipe.servings

			if updated_recipe.difficulty is not None:
				recipe.difficulty = updated_recipe.difficulty

			return {"Message:","Recipe Updated Successfully"}

	raise HTTPException(
		status_code=404,
		detail = "Recipe Not Found"
	)