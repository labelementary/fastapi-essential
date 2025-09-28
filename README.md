# FastAPI Essential

FastAPI Essential, Pre-Configured FastAPI Project with all essential dependencies and configurations for a robust and scalable FastAPI application.

## Project Setup

Follow these steps to set up your development environment for the first time.

### Prerequisites

*   Python 3.12 or newer.
*   [UV](https://github.com/astral-sh/uv) installed. This project uses `uv` for package and environment management.

### First-Time Installation

1.  **Clone the Repository**
    ```bash
    git clone <your-repository-url>
    cd fastapi-essential
    ```

2.  **Install All Dependencies**
    Run the following single command. It will automatically create a virtual environment, install all production and development dependencies, and install the project itself in "editable" mode.
    ```bash
    uv sync --dev
    ```
    This command creates a `uv.lock` file, which should be committed to your repository to ensure all developers use the exact same package versions.

3.  **Initialize Pre-Commit Hooks**
    Set up pre-commit hooks to automatically format and lint your code before each commit. This is crucial for maintaining code quality.
    ```bash
    uv run pre-commit install
    ```

## Development Workflow

### Running the Application

To start the FastAPI development server with live reloading, run:

```bash
uv run uvicorn src.main:app --reload --port 7070
```
or use the following command:

```bash
uv run fastapi dev ./src/main.py --reload --port 7070
```

*   `uvicorn` is the ASGI server that runs your FastAPI application.
*   `src.main:app` points to the `app` object inside the `src/main.py` file.
*   `--reload` automatically restarts the server when you make code changes.

### Daily Dependency Management

To ensure your local environment is perfectly synchronized with the project's lock file (`uv.lock`), especially after pulling changes from git, run:

```bash
uv sync --dev
```
This command installs any new packages and, importantly, removes any that are no longer required, preventing environment conflicts.

## Code Quality Tools

While pre-commit handles checks automatically, you can—and should—run these tools manually to format your code and get immediate feedback.

### 1. Linting and Formatting with Ruff

Ruff is an extremely fast linter and code formatter.

*   **Format your code:**
    This command reformats all files in the `src` directory to match the project's style.
    ```bash
    uv run ruff format src
    ```

*   **Check for errors and auto-fix them:**
    This command finds potential bugs and style issues, and automatically fixes anything it can.
    ```bash
    uv run ruff check src --fix
    ```

### 2. Static Type Checking with Pyright

Pyright checks your code for type errors, helping you catch bugs before you even run the application.

*   **Run a one-time check:**
    ```bash
    uv run pyright
    ```
    If there are no errors, the command will finish silently. Otherwise, it will print a detailed report.

*   **Run in "watch" mode for live feedback (Recommended):**
    This command provides instant feedback in your terminal every time you save a file.
    ```bash
    uv run pyright --watch
    ```

## Folder Structure

The project is organized using a modern `src` layout.

```
/fastapi-essential
├── .github/             # GitHub Actions workflows
├── .venv/               # Virtual environment managed by uv
├── alembic/             # Alembic database migration scripts
├── src/                 # Main application source code
│   ├── configs/         # Configuration (database, settings)
│   ├── functions/       # Business logic and services
│   ├── models/          # SQLAlchemy ORM models
│   ├── routes/          # API endpoint definitions (routers)
│   │   └── v1/
│   ├── __init__.py
│   └── main.py          # FastAPI application entry point
├── tests/               # Unit and integration tests
├── .gitignore
├── .pre-commit-config.yaml # Configuration for pre-commit hooks
├── pyproject.toml       # Project metadata, dependencies, and tool configs (Ruff, Pyright)
├── README.md            # This file
└── uv.lock              # Lockfile for reproducible builds```

*   **`src/`**: All the application's Python code lives here. This separation prevents common import issues.
*   **`alembic/`**: Handles database schema migrations.
*   **`pyproject.toml`**: The single configuration file for the entire project. It defines dependencies and configures tools like Ruff and Pyright.
*   **`uv.lock`**: A lockfile that guarantees identical environments for all developers and in production.
