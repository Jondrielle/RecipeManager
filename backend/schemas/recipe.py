from pydantic import BaseModel
from typing import Optional
from enums.difficulty import Difficulty

class Recipe(BaseModel):
	id: int
	name: str
	description:Optional[str] = None
	ingredients:list[str]
	instructions:str
	prep_time:int
	cook_time:int
	servings:int
	difficulty: Difficulty

class CreateRecipe(BaseModel):
	name: str
	description:Optional[str] = None
	ingredients:list[str]
	instructions:str
	prep_time:int
	cook_time:int
	servings:int
	difficulty: Difficulty

class RecipeResponse(BaseModel):
	id: int