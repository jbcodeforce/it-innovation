import json
from dotenv import load_dotenv
import os
from deta import Deta

load_dotenv(dotenv_path=".streamlit/secrets.toml")
DETA_KEY=os.getenv("DETA_TOKEN")

deta = Deta(DETA_KEY)
db = deta.Base("users")

def insert_user(username, name, email, password):
    return db.put({"key": username, "name": name, "pwd": password, "email": email})

insert_user("bbuilder","bob the builder", "bbluider@email.com", "secret")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)