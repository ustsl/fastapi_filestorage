import os

from dotenv import load_dotenv
from envparse import Env

env = Env()

load_dotenv()


#### LOAD ENV DATA

SERVICE_TOKEN = os.getenv("SERVICE_TOKEN")
