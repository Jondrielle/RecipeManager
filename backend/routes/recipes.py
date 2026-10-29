from typing import Annotated

from database import get_session
from fastapi import APIRouter, Depends, HTTPException
from models.recipe import Recipe as RecipeModel
from schemas.recipe import CreateRecipe, UpdateRecipe
from schemas.recipe import Recipe as RecipeSchema
from sqlmodel import Session, select

recipe_router = APIRouter()

sessionDeps = Annotated[Session,Depends(get_session)]

@recipe_router.get("/", response_model=list[RecipeSchema])
async def get_recipes(session: sessionDeps):
    return session.exec(select(RecipeModel)).all()

@recipe_router.post("/recipe", response_model=RecipeSchema)
async def add_recipe(recipe:CreateRecipe,session:  sessionDeps):

    new_recipe = RecipeModel(
        name = recipe.name,
        description = recipe.description,
        ingredients=[
            {
                "name": ingredient.name,
                "amount": ingredient.amount,
                "unit": ingredient.unit.value
            }
            for ingredient in recipe.ingredients
        ],
        instructions = recipe.instructions,
        prep_time = recipe.prep_time,
        cook_time = recipe.cook_time,
        servings = recipe.servings,
        difficulty = recipe.difficulty,
        image_url = recipe.image_url
    )

    session.add(new_recipe)
    session.commit()
    session.refresh(new_recipe)

    return new_recipe

@recipe_router.delete("/recipe/{id}")
async def delete_recipe(id:int, session:  sessionDeps):

    recipe = session.get(RecipeModel, id)
    
    if not recipe:
        raise HTTPException(
            status_code = 404,
            detail = "Recipe Not Found"
        )

    session.delete(recipe)
    session.commit()

    return {"message": "Recipe Deleted Successfully"}

@recipe_router.patch("/recipes/{id}")
async def update_recipe(id:int, updated_recipe:UpdateRecipe, session: sessionDeps):
    recipe = session.get(RecipeModel, id)
    
    if not recipe:
        raise HTTPException(
            status_code=404,
            detail="Recipe Not Found"
        )

    if updated_recipe.name is not None:
        recipe.name = updated_recipe.name

    if updated_recipe.description is not None:
        recipe.description = updated_recipe.description

    if updated_recipe.ingredients is not None:
        recipe.ingredients = [
            {
                "name": ingredient.name,
                "amount": ingredient.amount,
                "unit": ingredient.unit.value
            }
            for ingredient in updated_recipe.ingredients
        ]

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

    if updated_recipe.image_url is not None:
        recipe.image_url = updated_recipe.image_url

    session.add(recipe)
    session.commit()
    session.refresh(recipe)

    return recipe