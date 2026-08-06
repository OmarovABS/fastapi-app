import os
from dotenv import load_dotenv
from authx import AuthX, AuthXConfig

load_dotenv()

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


config = AuthXConfig()
config.JWT_SECRET_KEY = "ADMIN_SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)