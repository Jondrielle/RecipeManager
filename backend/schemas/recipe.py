from pydantic import BaseModel,Optional
from enums.difficulty import Difficulty


class Recipe(BaseModel):
	name: str
	description:Optional[str] = None
	ingredients:str[]
	instructions:str
	prep time:str
	cook time:str
	servings:int
	difficulty: Difficulty