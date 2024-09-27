import os
import nanoid
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


def nid(
    alphabet: str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-',
    size: int = 11
):
    return nanoid.generate(
        alphabet=alphabet,
        size=size
    )


@dataclass
class Bot:
    token: str


@dataclass
class Database:
    url: str
    expire_on_commit: bool


db_sqlite3 = Database('sqlite+aiosqlite:///db.sqlite3', False)
bot = Bot(os.getenv('BOT_TOKEN'))