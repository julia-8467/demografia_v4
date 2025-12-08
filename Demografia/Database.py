import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from . import config

TESTING = os.getenv("TESTING") == "1"

if TESTING:
    # Używamy SQLite w pamięci – zero problemów w CI
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
else:
    DATABASE_USERNAME = config.DATABASE_USERNAME
    DATABASE_PASSWORD = config.DATABASE_PASSWORD
    DATABASE_HOST = config.DATABASE_HOST
    DATABASE_NAME = config.DATABASE_NAME
    DATABASE_PORT = config.DATABASE_PORT

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}"
        f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
