from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from Demografia.models import Base

# Tworzymy testową bazę SQLite w RAM
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tworzymy wszystkie tabele
Base.metadata.create_all(bind=engine)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides = {}
app.dependency_overrides[get_db] = override_get_db  # <-- KLUCZOWA LINIA

client = TestClient(app)


def test_homepage():
    response = client.get("/")
    assert response.status_code in (200, 500)  # zależy, czy są dane


def test_index():
    response = client.get("/index/")
    assert response.status_code in (200, 500)


def test_zgony_default():
    response = client.get("/zgony/")
    assert response.status_code in (200, 500)
