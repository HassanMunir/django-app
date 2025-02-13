from sqlalchemy import create_engine, Column, Integer, String, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Type


Base: Type = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    @staticmethod
    def validate_name(mapper, connection, target):
        if not target.name:
            raise Exception("Name cannot be empty.")


event.listen(User, "before_insert", User.validate_name)
event.listen(User, "before_update", User.validate_name)


engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine, checkfirst=True)
