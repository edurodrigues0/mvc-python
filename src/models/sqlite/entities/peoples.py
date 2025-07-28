from sqlalchemy import Column, String, BIGINT, ForeignKey
from src.models.sqlite.settings.base import Base

class PeoplesTable(Base):
  __tablename__ = "peoples"

  id = Column(BIGINT, primary_key=True, autoincrement=True)
  firs_name = Column(String(100), nullable=False)
  last_name = Column(String(100), nullable=False)
  age = Column(BIGINT, nullable=False)
  pet_id = Column(BIGINT, ForeignKey("pets.id"), nullable=True)

  def __repr__(self):
    return f'Peoples [first_name={self.firs_name}, age={self.age}, pet_id={self.pet_id}]'

  def __to_dict__(self):
    return {
      "id": self.id,
      "first_name": self.firs_name,
      "last_name": self.last_name,
      "age": self.age,
      "pet_id": self.pet_id
    }
