from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from src.configs.model import Base
import os
from dotenv import load_dotenv
from alembic import context

# Load Environment Variables
load_dotenv()

# Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your model's MetaData object here
target_metadata = Base.metadata

# Set the SQLAlchemy URL from the environment variable PG_URL - For Async pg
pg_url = os.getenv('PG_URL')
if pg_url:
    sync_pg_url = pg_url.replace('asyncpg', 'psycopg2')
    config.set_main_option('sqlalchemy.url', sync_pg_url)
else:
    raise ValueError("PG_URL environment variable is not set. Please set it to your database URL.")

# Function to Handle Migrations Offline
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Function to Run Migrations Online
def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

# Run the appropriate migration function based on the mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
