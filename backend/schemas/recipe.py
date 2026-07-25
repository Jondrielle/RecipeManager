from pydantic import BaseModel
from enums.difficulty import Difficulty

class Recipe(BaseModel):
	name: str
	description:str
	ingredients:str[]
	instructions:str
	prep time:str
	cook time:str
	servings:int
	difficulty: Difficulty