from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel
from config import engine
from routes import router
from models import *
from fastapi.responses import JSONResponse

app = FastAPI()

@app.on_event("startup")
def startup_event():
    with engine.begin() as conn:
        SQLModel.metadata.create_all(bind=conn)

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    """
    Handle ValueError exceptions raised by the application.

    Args:
        request: The request that caused the exception.
        exc: The exception instance.

    Returns:
        A JSONResponse with a status code of 400 (Bad Request) and a body containing the error message.
    """
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": str(exc)},
    )

app.mount("/templates/static", StaticFiles(directory="templates/static"), name="static")

app.include_router(router)