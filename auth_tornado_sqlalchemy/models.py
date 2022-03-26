from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

DB = 'mysql+mysqldb://reganto:540689m$@127.0.0.1:3306/testdb'
engine = create_engine(DB)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(200), nullable=False, unique=True)
    password = Column(String(200), nullable=False)


# Base.metadata.create_all(engine)