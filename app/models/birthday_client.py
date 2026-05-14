from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class BirthdayClient(Base):

    __tablename__ = "birthday_clients"

    id = Column(Integer, primary_key=True, index=True)

    phone = Column(String, unique=True)

    ddd = Column(String)

    first_name = Column(String)

    last_name = Column(String)

    cpf = Column(String, nullable=True)

    value = Column(String, nullable=True)