import os, dotenv, pathlib

dotenv.load_dotenv()

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
WORDBANK_DIR = os.path.join(SETTINGS_DIR, "wordbank")

TOKEN = os.getenv("TOKEN")