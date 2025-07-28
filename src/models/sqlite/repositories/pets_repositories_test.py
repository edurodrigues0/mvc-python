import pytest
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Database interaction tests should be run with a test database setup.")
def test_get_all_pets():
  repo = PetsRepository(db_connection_handler)
  response = repo.get_all_pets()
  print(response)
  assert isinstance(response, list)
  assert len(response) > 0

@pytest.mark.skip(reason="Database interaction tests should be run with a test database setup.")
def test_get_pet_by_id():
  repo = PetsRepository(db_connection_handler)
  pet_id = 1
  response = repo.get_pet_by_id(pet_id)
  assert isinstance(response, PetsTable)
  assert response.name == "cao"
  assert response.type == "dog"

@pytest.mark.skip(reason="Database interaction tests should be run with a test database setup.")
def test_add_pet():
  repo = PetsRepository(db_connection_handler)
  new_pet = PetsTable(name="Osvaldo", type="cat")
  response = repo.add_pet(new_pet)
  assert isinstance(response, PetsTable)
  assert response.name == "Osvaldo"
  assert response.type == "cat"

@pytest.mark.skip(reason="Database interaction tests should be run with a test database setup.")
def test_delete_pets():
  repo = PetsRepository(db_connection_handler)
  pet_id = 2
  repo.delete_pets(pet_id)
  response = repo.get_pet_by_id(pet_id)
  assert response is None
