import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from database import get_session
from enums.difficulty import Difficulty
from main import app


@pytest.fixture(name="session")
def session_fixture():
	test_engine = create_engine("sqlite://",
		connect_args={"check_same_thread":False},
		poolclass=StaticPool,
	)

	SQLModel.metadata.create_all(test_engine)

	with Session(test_engine) as session:
		yield session

	test_engine.dispose()

@pytest.fixture
def client(session):
	def get_session_override():
		yield session

	app.dependency_overrides[get_session] = get_session_override

	test_client = TestClient(app)
	yield test_client

	app.dependency_overrides.clear()

def test_get_recipes(client):
	response = client.get("/")
	
	assert response.status_code == 200
	assert response.json() == []

def test_create_valid_recipe(client):
	response = client.post(
		"/recipe",
		json={
			"name": "Red beans and rice",
			"servings": 3,
			"prep_time": 20,
			"cook_time": 300,
			"difficulty": Difficulty.HARD.value,
			"ingredients": [
				{
					"name": "Rice",
					"amount": 2,
					"unit": "cup"
				}
			],
			"instructions": [
				"Rinse the rice",
				"Cook the rice"
			]
		}
	)

	assert response.status_code == 200
	assert response.json()["name"] == "Red beans and rice"

def test_create_invalid_recipe(client):
	response = client.post("/recipe",
		json={
			"name": "Red beans and rice",
			"servings": 3,
			"prep_time": 20,
		})

	assert response.status_code == 422

def test_delete_nonexistent_recipe(client):
	response = client.delete("/recipe/1000")

	assert response.status_code == 404

def test_delete_existent_recipe(client):
	create_response = client.post("/recipe",
		json={
			"name": "Rice",
			"servings": 3,
			"prep_time": 20,
			"cook_time": 300,
			"difficulty": Difficulty.EASY.value,
			"ingredients": [
				{
					"name": "Rice",
					"amount": 2,
					"unit": "cup"
				},
				{
					"name": "Water",
					"amount": 3,
					"unit": "cup"
				}
			],
			"instructions": [
				"Rinse the rice",
				"Cook the rice",
				"Serve the rice"
			]
		})

	assert create_response.status_code == 200

	recipe_id = create_response.json()["id"]

	response = client.delete(f"/recipe/{recipe_id}")

	assert response.status_code == 200

def test_update_recipe_single_field_name(client):
	create_response = client.post("/recipe",
		json={
			"name": "Rice",
			"servings": 3,
			"prep_time": 20,
			"cook_time": 300,
			"difficulty": Difficulty.EASY.value,
			"ingredients": [],
			"instructions": []
		})
	assert create_response.status_code == 200
	assert create_response.json()["name"] == "Rice"
	recipe_id = create_response.json()["id"]


	response = client.patch(f"/recipes/{recipe_id}",
		json={
			"name": "Fried cabbage"
		})

	assert response.status_code == 200
	assert response.json()["name"] == "Fried cabbage"

def test_update_recipe_multiple_fields(client):
	create_response = client.post("/recipe",
		json={
			"name": "Rice",
			"servings": 5,
			"prep_time": 2,
			"cook_time": 20,
			"difficulty": Difficulty.EASY.value,
			"ingredients": [],
			"instructions": []
		})

	assert create_response.status_code == 200
	recipe_id = create_response.json()["id"]

	response = client.patch(f"/recipes/{recipe_id}",
		json={
			"name": "Rice and peas",
			"servings": 4,
			"prep_time":4,
			"cook_time":15,
			"difficulty":Difficulty.MEDIUM.value,
			"ingredients": [
				{
					"name": "Rice",
					"amount": 3,
					"unit": "cup"
				},
				{
					"name": "Pigeon peas",
					"amount": 1,
					"unit": "cup"
				}
			],
			"instructions":[
				"Rinse rice",
				"Rinse pigeon peas",
				"Cook rice and peas",
				"Serve dish"
			]
		})

	recipe_data = response.json()

	assert response.status_code == 200

	assert recipe_data["name"] == "Rice and peas"
	assert recipe_data["servings"] == 4
	assert recipe_data["prep_time"] == 4
	assert recipe_data["cook_time"] == 15
	assert recipe_data["difficulty"] == Difficulty.MEDIUM
	assert recipe_data["ingredients"] == [{
					"name": "Rice",
					"amount": 3,
					"unit": "cup"
				},
				{
					"name": "Pigeon peas",
					"amount": 1,
					"unit": "cup"
				}]
	assert recipe_data["instructions"] == ["Rinse rice",
				"Rinse pigeon peas",
				"Cook rice and peas",
				"Serve dish"]



#Tests to do next:
#Get recipes after creating one	
#Update nonexistent recipe	
#Update with invalid data	
#Update with an empty request	
#Create recipe with missing required fields	Required fields are enforced
#Create recipe with invalid ingredient unit	Invalid enum values are rejected
#Delete a recipe, then retrieve recipes.Deleted recipe is no longer present
#Update only servings	