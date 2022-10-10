# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'localhost:5432'
db_name = 'social-media-generator'
db_user = 'postgres'
db_password = 's0cial-media-generator'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class TextEntity():
    id = Column(Integer, primary_key=True)
    added_at = Column(DateTime)

    def __init__(self):
        self.added_at = datetime.now()