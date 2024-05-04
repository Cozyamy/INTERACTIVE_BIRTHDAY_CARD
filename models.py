from sqlmodel import SQLModel, Field

class Wish(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    sender_name: str = Field(default=None)
    message: str = Field(default=None)