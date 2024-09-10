# Movie API

This API is built with FastAPI, it performs all CRUD operations on a SQLite database
for managing movies.

This is a playground project so it includes the autogenerated FastAPI documentation:
[API Documentation](https://movi-api.onrender.com/docs)

## Features

- **CRUD Operations**: Create, read, update, and delete movies.
- **Authentication**: JWT-based login system.
- **Batch Operations**: Insert multiple movies in a single request.

## Default login credentials

- email: `admin@gmail.com`
- password: `admin`

These credentials are automatically set in the example schema in the API docs.

## API Endpoints

| Method | Endpoint             | Description             |
|--------|----------------------|-------------------------|
| POST   | `/login`             | Login aunthentication   |
| GET    | `/movies`            | Get all movies          |
| GET    | `/movies/{movie_id}` | Get a movie by ID       |
| GET    | `/movies/{category}` | Get movies by category  |
| POST   | `/movies`            | Create a new movie      |
| POST   | `/movies/batch`      | Create multilple movies |
| PUT    | `/movies/{movie_id}` | Update a movie by ID    |
| DELETE | `/movies/{movie_id}` | Delete a movie by ID    |

## Running Locally

1. Clone the repository:

    ```bash
    git clone git@github.com:jeyg20/movie_api.git
    cd movie-api
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    uvicorn main:app
    ```

5. Access the API:

    - API Root: `http://127.0.0.1:8000`
    - API Documentation (Swagger UI): `http://127.0.0.1:8000/docs`
    - Alternative Documentation (ReDoc): `http://127.0.0.1:8000/redoc`
