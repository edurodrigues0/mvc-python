from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository

class MockConnectionHandler:
  def __init__(self) -> None:
    self.session = UnifiedAlchemyMagicMock(
      data=[
        (
          [mock.call.query(PetsTable)],
          [
            PetsTable(name="Rex", type="dog"),
            PetsTable(name="Mittens", type="cat")
          ],
        )
      ]
    )

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    pass

def test_get_all_pets():
  mock_connection = MockConnectionHandler()
  repository = PetsRepository(mock_connection)
  pets = repository.get_all_pets()

  mock_connection.session.query.assert_called_once_with(PetsTable)
  mock_connection.session.all.assert_called_once()
  mock_connection.session.filter.assert_not_called()

  assert len(pets) == 2
  assert pets[0].name == "Rex"
  assert pets[1].name == "Mittens"

def test_delete_pets():
  mock_connection = MockConnectionHandler()
  repository = PetsRepository(mock_connection)

  repository.delete_pets(1)

  mock_connection.session.query.assert_called_once_with(PetsTable)
  mock_connection.session.filter.assert_called_once_with(PetsTable.id == 1)
  mock_connection.session.delete.assert_called_once()
