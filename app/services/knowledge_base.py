"""Reviewed, concise educational answers for supported topics."""

KNOWLEDGE = {
    "sip": {
        "en": "A SIP (Systematic Investment Plan) lets you invest a fixed amount in a mutual fund at regular intervals. For example, ₹500 each month buys fund units at that month's price. Returns are market-linked and not guaranteed.",
        "hi": "SIP (सिस्टमैटिक इन्वेस्टमेंट प्लान) में आप म्यूचुअल फंड में नियमित अंतराल पर एक तय रकम लगाते हैं। जैसे हर महीने ₹500 लगाने पर उस महीने की कीमत के अनुसार यूनिट मिलती हैं। रिटर्न बाजार पर निर्भर है और तय नहीं है।",
    },
    "fd": {
        "en": "A fixed deposit (FD) keeps a lump sum with a bank for a chosen period at a stated interest rate. The rate and withdrawal rules vary by bank; check them before opening one. Example: ₹10,000 for a year earns interest according to the bank's terms.",
        "hi": "फिक्स्ड डिपॉज़िट (FD) में आप एक तय रकम बैंक में चुनी हुई अवधि के लिए रखते हैं। ब्याज दर और समय से पहले पैसे निकालने के नियम बैंक के अनुसार बदलते हैं। जमा करने से पहले शर्तें जाँचें।",
    },
    "interest": {
        "en": "Interest is the cost of borrowing money or the amount earned for saving or lending it. The rate, time period, and compounding method affect the amount. Always check whether a quoted rate is annual and whether it is simple or compound interest.",
        "hi": "ब्याज पैसे उधार लेने की लागत या बचत पर मिलने वाली रकम है। दर, समय और ब्याज जुड़ने का तरीका कुल रकम बदलते हैं। पूछें कि दर सालाना है या नहीं और ब्याज साधारण है या चक्रवृद्धि।",
    },
    "savings": {
        "en": "Saving means setting aside money for future needs. A simple starting point is to choose an affordable monthly amount and keep it separate from day-to-day spending. This app's savings estimate counts contributions only and excludes interest.",
        "hi": "बचत का मतलब भविष्य की ज़रूरतों के लिए पैसे अलग रखना है। अपनी क्षमता के अनुसार हर महीने रकम तय करें और उसे रोज़मर्रा के खर्च से अलग रखें। यहाँ बचत कैलकुलेटर केवल जमा रकम जोड़ता है, ब्याज नहीं।",
    },
    "emi": {
        "en": "An EMI (equated monthly instalment) is a regular monthly loan payment. It usually includes both principal and interest. Compare the total repayment, fees, rate type, and late-payment terms before borrowing.",
        "hi": "EMI यानी हर महीने दी जाने वाली तय किस्त। इसमें आम तौर पर मूलधन और ब्याज दोनों होते हैं। कर्ज लेने से पहले कुल भुगतान, फीस, ब्याज दर का प्रकार और देर से भुगतान की शर्तें समझें।",
    },
    "loan": {
        "en": "A loan is money borrowed that must be repaid, usually with interest and possibly fees. Before agreeing, check the total repayment, annual rate, instalment schedule, penalties, and whether the rate can change.",
        "hi": "लोन वह रकम है जो उधार ली जाती है और आम तौर पर ब्याज व संभावित फीस के साथ लौटानी होती है। सहमति से पहले कुल भुगतान, सालाना दर, किस्तें, जुर्माना और बदलती दर की शर्तें जाँचें।",
    },
    "insurance": {
        "en": "Insurance is a contract that may pay for specified losses in exchange for a premium, subject to its terms. Read exclusions, waiting periods, claim steps, coverage limits, and renewal conditions; coverage is not automatic for every event.",
        "hi": "बीमा एक अनुबंध है जिसमें प्रीमियम के बदले तय जोखिमों पर भुगतान मिल सकता है। अपवाद, प्रतीक्षा अवधि, दावा प्रक्रिया, कवरेज सीमा और नवीनीकरण की शर्तें पढ़ें; हर घटना कवर नहीं होती।",
    },
    "banking": {
        "en": "A bank account can help you receive and manage money. Check account fees, minimum-balance rules, service access, and official bank contact details. Never share your OTP, UPI PIN, CVV, password, or full card details with anyone.",
        "hi": "बैंक खाता पैसे पाने और संभालने में मदद करता है। खाते की फीस, न्यूनतम बैलेंस और सेवाओं की शर्तें जाँचें। OTP, UPI PIN, CVV, पासवर्ड या कार्ड की पूरी जानकारी किसी से साझा न करें।",
    },
}

EXAMPLES = {
    "en": ["What is a SIP?", "How does a fixed deposit work?", "What is EMI?", "How does insurance work?", "What does interest mean?"],
    "hi": ["SIP kya hota hai?", "Fixed deposit kaise kaam karta hai?", "EMI kya hai?", "Insurance kya hota hai?", "Byaaj ka matlab kya hai?"],
}

def answer_for(topic: str, language: str) -> str:
    """Return a reviewed answer, falling back to English for absent translations."""
    entry = KNOWLEDGE.get(topic)
    if not entry:
        return ""
    return entry.get(language, entry["en"])
