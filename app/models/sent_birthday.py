from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database import Base


class SentBirthday(Base):

    __tablename__ = "sent_birthdays"

    id = Column(Integer, primary_key=True, index=True)

    phone = Column(String, index=True)

    first_name = Column(String)

    sent_year = Column(Integer)

    sent_at = Column(
        DateTime,
        default=datetime.utcnow
    )