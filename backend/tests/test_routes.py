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

