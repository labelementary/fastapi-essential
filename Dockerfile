# Use a Python image with uv pre-installed (Python 3.11)
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

# Set the working directory
WORKDIR /app

# Enable bytecode compilation and set link mode
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Install system dependencies for PostgreSQL (psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml uv.lock /app/

# Sync dependencies without installing the project itself or dev dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Copy the entire application code
ADD . /app

# Sync dependencies including the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Set the virtual environment path and update PATH
ENV UV_PROJECT_ENVIRONMENT=/app/env
ENV PATH="/app/env/bin:$PATH"

# Expose the default port (can be overridden at runtime)
EXPOSE 8000

# Use a shell to evaluate the PORT variable, defaulting to 8000 if not set
CMD ["/bin/sh", "-c", "uv run uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 4"]
