# FASTAPI-ESSENTIAL

This is a FastAPI-based project that provides essential functionality for a web application.

## Getting Started

To get started with the Project M Backend, follow the steps below:

### 1. Install Dependencies

Run the following command to install the necessary dependencies:

```bash
uv sync
```

### 2. Activate the Virtual Environment

Activate the virtual environment using the following command:

```bash
.venv\Scripts\activate
```

### 3. Initialize the Pre-Commit Hooks

Run the following command to initialize pre-commit hooks to ensure consistent code formatting and linting before each commit:

```bash
uv run pre-commit install
```

### 4. Run the Application

Start the FastAPI development server with the following command:

```bash
uv run fastapi dev ./src/main.py
```

This will run the FastAPI application with live reloading enabled.

## Before Committing

Ensure that your code is properly formatted and passes linting before committing by running these commands:

### 1. Format the Code

```bash
uv run ruff format .
```

### 2. Check Linting

```bash
uv run ruff check .
```

## Folder Structure

The folder structure of the project is organized as follows:

```bash

/project-root
    .github                 # GitHub-related files
    .vscode                 # Visual Studio Code-related files
    /src
        /routes            # Contains all the API route definitions
            root.py        # Root route and basic endpoints
            users.py       # Example of additional route files
        /models            # Contains ORM models and database schemas
            user.py        # User model
            post.py        # Post model
        /config            # Configuration files for the app
            settings.py    # Settings for environment variables
            database.py    # Database connection configuration
        /hooks             # Custom hooks or utility functions
    /tests                 # Contains unit tests and integration tests
    .editorconfig          # Defines coding styles between different editors and IDEs
    .gitattributes         # Defines attributes for files
    .gitignore             # Specifies files to ignore in Git
    .pre-commit-config.yaml # Configuration file for pre-commit hooks
    .python-version        # Specifies the Python version used by the project
    build.py               # Build script for the application
    ruff.toml              # Configuration file for the Ruff linter and formatter
    pyproject.toml         # Project configurations and dependencies
    README.md              # Project documentation
    LICENSE                # License information
```

### Routes

- **/routes**: Contains all the route files where API endpoints are defined. Each route file corresponds to a feature or resource of the application (e.g., `root.py`, `users.py`).

### Models

- **/models**: Contains the database models that define the structure of your data in the database (e.g., `user.py`, `post.py`).

### Config

- **/config**: Contains configuration files for various services and settings such as database connection, environment variables, etc. (e.g., `settings.py`, `database.py`).

### Hooks

- **/hooks**: Contains custom utility functions or hooks that are shared across different parts of the application.

## License

This project is licensed under the **Private License**. The copyright and ownership rights to the code are solely held by the project owner.
