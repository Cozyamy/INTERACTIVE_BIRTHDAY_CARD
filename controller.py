from config import engine
from sqlmodel import Session

def get_session():
    return Session(engine)