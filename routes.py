from fastapi import APIRouter, Response
from sqlmodel import select
from fastapi.responses import HTMLResponse
from models import Wish
from controller import get_session

router = APIRouter()

@router.get("/wishes", response_model=list[Wish], summary="Get all wishes", description="Fetches all the wishes from the database.")
def read_wishes(response: Response):
    """
    Fetches all the wishes from the database and returns them as a list.
    Also sets the Cache-Control header to "no-store" to prevent caching.
    """
    session = get_session()
    wishes = session.exec(select(Wish)).all()
    response.headers["Cache-Control"] = "no-store"
    session.close()
    return wishes

@router.post("/wishes", response_model=Wish, summary="Create a new wish", description="Adds a new wish to the database.")
def create_wish(wish: Wish):
    """
    Adds a new wish to the database.
    The wish must be provided in the request body as a JSON object with "sender_name" and "message" properties.
    """
    if wish.sender_name is None:
        raise ValueError("sender_name cannot be None")
    session = get_session()
    session.add(wish)
    session.commit()
    session.refresh(wish)
    session.close()
    return wish

@router.get("/", response_class=HTMLResponse, summary="Get the main page", description="Returns the HTML for the main page.")
async def read_item():
    """
    Returns the HTML for the main page.
    """
    with open("templates/index.html") as f:
        return f.read()
    
@router.get("/wishes_page", response_class=HTMLResponse, summary="Get the wishes page", description="Returns the HTML for the wishes page.")
async def read_wishes_page():
    """
    Returns the HTML for the wishes page.
    """
    with open("templates/wishes.html") as f:
        return f.read()