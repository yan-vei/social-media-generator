import os
from sys import platform
SLASH = '\\' if platform == "win32" else '/'

POSTGRES_URL = "localhost"
if (container_name := os.environ.get('DB_CONTAINER_NAME')):
    POSTGRES_URL = container_name