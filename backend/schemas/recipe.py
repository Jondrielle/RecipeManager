
from enums.difficulty import Difficulty
from enums.unit import Unit
from pydantic import BaseModel, Field


class Ingredient(BaseModel):
    name: str
    amount: float
    unit: Unit

class RecipeBase(BaseModel):
	name: str = Field(min_length=1,max_length=100)
	description:str | None = Field(default=None, max_length=500)
	ingredients:list[Ingredient]
	instructions:list[str]
	prep_time:int = Field(ge=0)
	cook_time:int = Field(ge=0)
	servings:int = Field(gt=0)
	difficulty: Difficulty
	image_url:str | None = None

class Recipe(RecipeBase):
	id: int

class CreateRecipe(RecipeBase):
	pass

class UpdateRecipe(BaseModel):
	name: str | None = Field(default=None,min_length=1,max_length=100)
	description:str | None = Field(default=None,max_length=500)
	ingredients:list[Ingredient] | None = None
	instructions:list[str] | None = None
	prep_time:int | None = Field(default=None,ge=0)
	cook_time:int | None = Field(default=None,ge=0)
	servings:int | None = Field(default=None,gt=0)
	difficulty: Difficulty | None = None
	image_url:str | None = None