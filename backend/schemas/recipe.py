from pydantic import BaseModel
from typing import Optional
from enums.difficulty import Difficulty

class RecipeBase(BaseModel):
	name: str
	description:Optional[str] = None
	ingredients:list[str]
	instructions:str
	prep_time:int
	cook_time:int
	servings:int
	difficulty: Difficulty

class Recipe(RecipeBase):
	id: int

class CreateRecipe(RecipeBase):
	pass

class UpdateRecipe(BaseModel):
	name: Optional[str] = None
	description:Optional[str] = None
	ingredients:Optional[list[str]] = None
	instructions:Optional[str] = None
	prep_time:Optional[int] = None
	cook_time:Optional[int] = None
	servings:Optional[int] = None
	difficulty: Optional[Difficulty] = None