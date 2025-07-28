from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable

class PetsRepository:
  def __init__(self, db_connection) -> None:
    self.__db_connection = db_connection

  def get_all_pets(self) -> list[PetsTable]:
    with self.__db_connection as database:
      try:
        pets = database.session.query(PetsTable).all()
        return pets
      except NoResultFound:
        return []

  def get_pet_by_id(self, pet_id: int) -> PetsTable | None:
    with self.__db_connection as database:
      try:
        pet = database.session.query(PetsTable).filter(PetsTable.id == pet_id).one()
        return pet
      except NoResultFound:
        return None

  def add_pet(self, pet: PetsTable) -> PetsTable:
    with self.__db_connection as database:
      try:
        database.session.add(pet)
        database.session.commit()
        database.session.refresh(pet)
        return pet
      except Exception as e:
        database.session.rollback()
        raise e

  def delete_pets(self, pet_id: int) -> None:
    with self.__db_connection as database:
      try:
        database.session.query(PetsTable).filter(PetsTable.id == pet_id).delete()
        database.session.commit()
      except Exception as e:
        database.session.rollback()
        raise e
