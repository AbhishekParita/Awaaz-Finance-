import pytest

from app.services.intent_router import route_message

@pytest.mark.parametrize("message,topic", [
    ("What is a SIP?", "sip"), ("SIP kya hota hai?", "sip"),
    ("Fixed deposit kaise kaam karta hai?", "fd"), ("What is EMI?", "emi"),
    ("How do I save money?", "savings"), ("loan kya hai", "loan"),
    ("How does insurance work?", "insurance"), ("ब्याज क्या है", "interest"),
    ("How does my bank account work?", "banking"),
])
def test_known_topics(message, topic):
    result = route_message(message)
    assert result == {"intent": "explain", "topic": topic}

def test_calculator_intent():
    assert route_message("I want an EMI calculator") == {"intent": "calculate", "topic": "emi"}

def test_unknown_and_sensitive_queries():
    assert route_message("Tell me today's lottery number")["intent"] == "fallback"
    assert route_message("Should I share my UPI PIN?") == {"intent": "safety", "topic": "credentials"}
