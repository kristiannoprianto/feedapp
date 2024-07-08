from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import apps
from .. import main
from app.database import Base, get_db  # Adjust the import based on your project structure
import pytest
import os

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Use an in-memory SQLite database for testing

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override for testing
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

apps.dependency_overrides[get_db] = override_get_db

client = TestClient(apps)

@pytest.fixture(scope="module")
def test_db():
    # Setup: Create the test database
    Base.metadata.create_all(bind=engine)
    yield
    # Teardown: Drop the test database
    Base.metadata.drop_all(bind=engine)
    os.remove("./test.db")

@pytest.fixture(scope="module")
def test_client():
    yield client

def test_save_rating_low(test_client, test_db):
    response = test_client.post(
        "/feedback/",
        json={"rating": 4}
    )
    assert response.status_code == 201

def test_save_rating_high(test_client, test_db):
    response = test_client.post(
        "/feedback/",
        json={"rating": 5}
    )
    assert response.status_code == 201

def test_outbound_value(test_client, test_db):
    response = test_client.post(
        "/feedback/",
        json={"rating": -1}
    )

    assert response.status_code == 422
