import os, dotenv, pathlib

dotenv.load_dotenv()

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
WORDBANK_DIR = os.path.join(SETTINGS_DIR, "wordbank")

TOKEN = os.getenv("TOKEN")

REDDIT_ID = os.getenv("REDDIT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")

NSFW_CHANNEL = os.getenv("NSFW_CHANNEL")

FILOU = os.getenv("FILOU")
RURU = os.getenv("RURU")
ALESS = os.getenv("ALESS")
CORBIN = os.getenv("CORBIN")
BRIDO = os.getenv("BRIDO")
PEPI = os.getenv("PEPI")
MARTIN = os.getenv("MARTIN")
REN = os.getenv("REN")
PHIL = os.getenv("PHIL")

DB = os.getenv("DB")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
CONN_STRING = os.getenv("CONN_STRING")




# Spotify function enabled
SP_ENABLE = False
