from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = 'localhost:5432'
db_name = 'social-media-generator'
db_user = 'postgres'
db_password = 's0cial-media-generator'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()
