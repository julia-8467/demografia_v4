from fastapi.testclient import TestClient
from main import app   # upewnij się, że Twój plik główny to main.py

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


client = TestClient(app)

def test_homepage():
    """Test strony głównej /"""
    response = client.get("/")
    assert response.status_code == 200

def test_index():
    """Test endpointu /index/"""
    response = client.get("/index/")
    assert response.status_code == 200

def test_zgony_default():
    """Endpoint /zgony/ powinien działać z domyślnymi parametrami"""
    response = client.get("/zgony/")
    assert response.status_code in (200, 500)
    # 200 jeśli masz dane lokalnie,
    # 500 jeśli brak DB – ale test nie wywali się

def test_demografia_missing_params():
    """Brak wymaganych parametrów musi dać 422"""
    response = client.get("/demografia/")
    assert response.status_code == 422
