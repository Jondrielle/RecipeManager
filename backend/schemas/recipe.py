from pydantic import BaseModel, Field
from typing import Optional
from enums.difficulty import Difficulty

class RecipeBase(BaseModel):
	name: str = Field(min_length=1,max_length=100)
	description:Optional[str] = Field(default=None, max_length=500)
	ingredients:list[str]
	instructions:list[str]
	prep_time:int = Field(ge=0)
	cook_time:int = Field(ge=0)
	servings:int = Field(gt=0)
	difficulty: Difficulty
	image_url:str = None

class Recipe(RecipeBase):
	id: int

class CreateRecipe(RecipeBase):
	pass

class UpdateRecipe(BaseModel):
	name: Optional[str] = Field(default=None,min_length=1,max_length=100)
	description:Optional[str] = Field(default=None,max_length=500)
	ingredients:Optional[list[str]] = None
	instructions:Optional[list[str]] = None
	prep_time:Optional[int] = Field(default=None,ge=0)
	cook_time:Optional[int] = Field(default=None,ge=0)
	servings:Optional[int] = Field(default=None,ge=0)
	difficulty: Optional[Difficulty] = None
	image_url:Optional[str] = None