from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def fetch_data(query):
    with engine.connect() as conn:
        result = conn.execute(query)
        return [dict(row) for row in result]