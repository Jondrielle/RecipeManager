from sqlmodel import Field, SQLModel
from enums.difficulty import Difficulty
from enums.unit import Unit
from typing import Optional
from sqlalchemy import Column, JSON

class Ingredient(SQLModel):
	name: str
	amount: float
	unit: Unit

class Recipe(SQLModel, table=True):
	id: int = Field(default=None,primary_key=True)
	name: str = Field(min_length=1,max_length=100)
	description: Optional[str] = Field(default=None,max_length=500)
	ingredients: list = Field(
        sa_column=Column(JSON)
    )
    instructions: list = Field(
        sa_column=Column(JSON)
    )
	prep_time:int = Field(ge=0)
	cook_time:int = Field(ge=0)
	servings:int = Field(gt=0)
	difficulty: Difficulty
	image_url: Optional[str] = None
