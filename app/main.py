"""FastAPI application for the Awaaz Finance MVP."""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.schemas import AskRequest, CalculateRequest
from app.services.calculators import CALCULATORS
from app.services.intent_router import route_message
from app.services.knowledge_base import EXAMPLES, answer_for

ROOT = Path(__file__).parent
STATIC = ROOT / "static"
app = FastAPI(title="Awaaz Finance", version="1.0.0", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=STATIC), name="static")

@app.get("/", include_in_schema=False)
def home() -> FileResponse:
    return FileResponse(STATIC / "index.html")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/api/examples")
def examples(language: str = "en") -> dict[str, object]:
    if language not in EXAMPLES:
        raise HTTPException(status_code=422, detail="Language must be 'en' or 'hi'.")
    return {"language": language, "examples": EXAMPLES[language]}

@app.post("/api/ask")
def ask(request: AskRequest) -> dict[str, str]:
    result = route_message(request.message)
    intent, topic, language = result["intent"], result["topic"], request.language
    if intent == "safety":
        answer = ("Never share your OTP, UPI PIN, CVV, password, or banking credentials with anyone. I do not need them." if language == "en"
                  else "अपना OTP, UPI PIN, CVV, पासवर्ड या बैंक की जानकारी किसी से साझा न करें। मुझे इनकी ज़रूरत नहीं है।")
    elif intent == "fallback":
        answer = ("I can help with basic banking, savings, interest, FD, SIP, EMI, loans, and insurance concepts. Try one of the sample questions." if language == "en"
                  else "मैं बैंकिंग, बचत, ब्याज, FD, SIP, EMI, लोन और बीमा की बुनियादी जानकारी दे सकता हूँ। कोई नमूना सवाल पूछकर देखें।")
    elif intent == "calculate":
        answer = (f"I can help calculate {topic.upper()}. Choose its calculator, enter the values, review them, and confirm before calculating." if language == "en"
                  else f"मैं {topic.upper()} की गणना में मदद कर सकता हूँ। कैलकुलेटर चुनें, रकम भरें, जाँचें और गणना से पहले पुष्टि करें।")
    else:
        answer = answer_for(topic, language)
    follow_up = ("Would you like to see a simple example?" if language == "en" else "क्या आप एक आसान उदाहरण देखना चाहेंगे?")
    return {"answer": answer, "intent": intent, "topic": topic, "language": language, "suggested_follow_up": follow_up}

@app.post("/api/calculate")
def calculate(request: CalculateRequest) -> dict:
    values = request.model_dump(exclude={"calculator"}) if hasattr(request, "model_dump") else request.dict(exclude={"calculator"})
    required = {
        "savings": ("monthly_amount", "months"),
        "fd": ("principal", "annual_rate_percent", "months"),
        "emi": ("principal", "annual_rate_percent", "months"),
        "sip": ("monthly_amount", "annual_assumed_rate_percent", "months"),
    }[request.calculator]
    missing = [name for name in required if values.get(name) is None]
    if missing:
        raise HTTPException(status_code=422, detail=f"Missing required field(s) for {request.calculator}: {', '.join(missing)}.")
    try:
        if request.calculator == "savings":
            result = CALCULATORS["savings"](request.monthly_amount, request.months)
        elif request.calculator == "fd":
            result = CALCULATORS["fd"](request.principal, request.annual_rate_percent, request.months)
        elif request.calculator == "emi":
            result = CALCULATORS["emi"](request.principal, request.annual_rate_percent, request.months)
        else:
            result = CALCULATORS["sip"](request.monthly_amount, request.annual_assumed_rate_percent, request.months)
        return result
    except (ValueError, OverflowError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
