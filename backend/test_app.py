import pytest
import os
from app import app

@pytest.mark.skipif(
    os.getenv("RUN_DB_TESTS") != "true",
    reason="DB not available"
)
def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200