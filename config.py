from sqlmodel import SQLModel, create_engine

sqlite_url = "sqlite:///./database.sqlite"
engine = create_engine(sqlite_url)

SQLModel.metadata.create_all(engine)