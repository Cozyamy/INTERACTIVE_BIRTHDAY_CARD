# Interactive Birthday Card

This is a FastAPI project that serves as an interactive birthday card. Users can add their wishes to a database, and these wishes can be viewed on a dedicated page.

## Project Structure

- `main.py`: The entry point of the application. It creates the FastAPI application instance and includes the routes from `routes.py`.
- `routes.py`: Defines the API routes for the application. It includes routes for adding wishes to the database and fetching all wishes.
- `models.py`: Defines the SQLModel models used in the application.
- `config.py`: Contains configuration for the application, such as the database engine.
- `controller.py`: Contains helper functions for database operations and reading template files.

## API Endpoints

- `GET /`: Returns the HTML for the main page.
- `GET /wishes_page`: Returns the HTML for the wishes page.
- `GET /wishes`: Fetches all the wishes from the database.
- `POST /wishes`: Adds a new wish to the database.

## How to Run the Project

1. Install the requirements:

```bash
poetry install
```

2. Run the application:

```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`.