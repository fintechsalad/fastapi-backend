import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.secrets'))

AUTH_SECRET_KEY = os.environ.get('AUTH_SECRET_KEY')