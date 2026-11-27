"""Small deterministic intent router; deliberately not a language model."""

import re

from app.services.knowledge_base import KNOWLEDGE

SAFETY_TERMS = re.compile(r"\b(otp|password|passcode|upi\s*pin|cvv|cvc|card\s*number|बैंक\s*पासवर्ड|ओटीपी|पिन)\b", re.I)
TOPIC_TERMS = {
    "sip": ("sip", "systematic investment", "एसआईपी", "सिप", "म्यूचुअल फंड", "mutual fund"),
    "fd": ("fixed deposit", "fixed-deposit", " fd", "fd ", "फिक्स्ड डिपॉजिट", "सावधि जमा"),
    "emi": ("emi", "ईएमआई", "किस्त"),
    "insurance": ("insurance", "बीमा", "bima"),
    "savings": ("saving", "savings", "बचत", "save money"),
    "interest": ("interest", "ब्याज", "byaj", "byaaj"),
    "loan": ("loan", "लोन", "कर्ज", "ऋण"),
    "banking": ("bank", "banking", "बैंक", "खाता", "account"),
}
CALCULATOR_TERMS = {
    "emi": ("calculate emi", "emi calculator", "calculate my emi", "ईएमआई निकाल", "किस्त निकाल"),
    "fd": ("fd calculator", "calculate fd", "fd maturity", "एफडी कैलकुलेटर"),
    "savings": ("savings calculator", "calculate savings", "बचत कैलकुलेटर"),
    "sip": ("sip calculator", "calculate sip", "sip returns", "एसआईपी कैलकुलेटर"),
}

def route_message(message: str) -> dict[str, str]:
    """Classify a question and return an intent/topic pair."""
    normalized = f" {message.casefold()} "
    if SAFETY_TERMS.search(message):
        return {"intent": "safety", "topic": "credentials"}
    for calculator, terms in CALCULATOR_TERMS.items():
        if any(term in normalized for term in terms):
            return {"intent": "calculate", "topic": calculator}
    for topic in KNOWLEDGE:
        if any(term in normalized for term in TOPIC_TERMS[topic]):
            return {"intent": "explain", "topic": topic}
    return {"intent": "fallback", "topic": "unknown"}
