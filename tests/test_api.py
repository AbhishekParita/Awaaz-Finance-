from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_home_health_and_examples():
    home = client.get("/")
    assert home.status_code == 200
    assert "Awaaz" in home.text
    assert client.get("/health").json() == {"status": "ok"}
    assert len(client.get("/api/examples?language=hi").json()["examples"]) > 0

def test_ask_known_unknown_and_sensitive():
    known = client.post("/api/ask", json={"message": "SIP kya hota hai?", "language": "hi"})
    assert known.status_code == 200 and known.json()["topic"] == "sip"
    unknown = client.post("/api/ask", json={"message": "weather please"})
    assert unknown.json()["intent"] == "fallback"
    safety = client.post("/api/ask", json={"message": "My OTP is 123456"})
    assert safety.json()["intent"] == "safety"
    assert "OTP" in safety.json()["answer"]

def test_api_calculators_and_invalid_payloads():
    result = client.post("/api/calculate", json={"calculator": "emi", "principal": 5000, "annual_rate_percent": 10, "months": 12})
    assert result.status_code == 200
    assert result.json()["monthly_emi"] == 439.58
    assert client.post("/api/calculate", json={"calculator": "fd", "principal": 0, "annual_rate_percent": 5, "months": 12}).status_code == 422
    assert client.post("/api/calculate", json={"calculator": "sip", "monthly_amount": 500}).status_code == 422
    assert client.post("/api/calculate", json={"calculator": "emi", "principal": 1000, "annual_rate_percent": 5, "months": 1.5}).status_code == 422
    assert client.post("/api/calculate", json={"calculator": "emi", "principal": True, "annual_rate_percent": 5, "months": 12}).status_code == 422
    assert client.post("/api/ask", json={"message": "x" * 501}).status_code == 422

def test_api_supports_all_calculators():
    requests = [
        {"calculator": "savings", "monthly_amount": 500, "months": 12},
        {"calculator": "fd", "principal": 10000, "annual_rate_percent": 6, "months": 12},
        {"calculator": "emi", "principal": 5000, "annual_rate_percent": 10, "months": 12},
        {"calculator": "sip", "monthly_amount": 500, "annual_assumed_rate_percent": 12, "months": 12},
    ]
    for request in requests:
        response = client.post("/api/calculate", json=request)
        assert response.status_code == 200
        assert response.json()["currency"] == "INR"
        assert response.json()["assumptions"]
