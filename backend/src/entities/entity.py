from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from utils.check_env import POSTGRES_URL
import config

db_url = f'{POSTGRES_URL}:5432'
db_name = config.db_name
db_user = config.db_user
db_password = config.db_password
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)
BCRYPT_LOG_ROUNDS = 13

Base = declarative_base()
