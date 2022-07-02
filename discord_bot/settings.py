import os, dotenv, pathlib
from pymongo import MongoClient

dotenv.load_dotenv()

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
WORDBANK_DIR = os.path.join(SETTINGS_DIR, "wordbank")

TOKEN = os.getenv("TOKEN")

REDDIT_ID = os.getenv("REDDIT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")

FILOU = os.getenv("FILOU")
RURU = os.getenv("RURU")

CLIENT = MongoClient('192.168.2.101', 30011)
DB = client['discord']
COLLECTION = db['wallet']