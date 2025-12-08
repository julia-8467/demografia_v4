import pytest
from fastapi.testclient import TestClient
from Demografia.Database import Base, engine, get_db, SessionLocal
from main import app

# 🔥 Tworzymy wszystkie tabele w testowej bazie SQLite
Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    # Nadpisujemy dependency, aby FastAPI używało testowego SessionLocal
    def override_get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
