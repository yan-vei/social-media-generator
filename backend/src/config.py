from dotenv import load_dotenv
import os

load_dotenv()

secret_key = os.environ.get('SECRET_KEY')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
