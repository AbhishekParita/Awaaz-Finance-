"use strict";

const copy = {
  en: {
    eyebrow: "MONEY, MADE EASIER", welcome: "Your money questions,<br>in your own words.",
    intro: "Ask about savings, loans, or insurance. We’ll explain it simply, one step at a time.", start: "LET’S START", how: "What would you like to know?", ask: "ASK",
    voiceNotice: "Voice input is handled by your browser’s speech service. Depending on your browser, audio may be processed by its provider. You can type instead.", tapSpeak: "Tap and speak", orType: "or type", questionLabel: "Your question", ready: "Ready when you are. Your words will appear here before we answer.", heard: "We heard:", edit: "Edit", askThis: "Ask this", tryAsk: "Try asking", yourAnswer: "YOUR ANSWER", listen: "Listen", explore: "EXPLORE A TOPIC", topics: "Start with what matters to you", chooseCard: "Choose a card to learn", banking: "Banking", bankingSub: "Accounts & basics", savings: "Savings", savingsSub: "Plan for tomorrow", loans: "Loans", loansSub: "Understand the cost", loans: "Loans", loansSub: "Understand the cost", insurance: "Insurance", insuranceSub: "Know your cover", tools: "SIMPLE TOOLS", calculators: "Try a calculator", illustrative: "Illustrative estimates, explained", savingsCalc: "Savings", savingsCalcSub: "Add up monthly contributions", fdCalc: "Fixed deposit", fdCalcSub: "Estimate maturity and interest", emiCalc: "EMI", emiCalcSub: "Understand a monthly instalment", sipCalc: "SIP estimate", sipCalcSub: "Explore an illustrative scenario", safeTitle: "Your safety comes first.", safeText: "We never need your OTP, UPI PIN, password, CVV, or bank details. This is for learning—not financial advice. Estimates are illustrative; returns are not guaranteed.", clear: "Clear conversation", localNote: "No conversation is saved after you leave this page.", listening: "Listening… say your question.", unsupported: "Speech recognition is not available in this browser. Please type your question or choose a sample.", noSpeech: "We didn’t catch that. Please try again or type your question.", micDenied: "Microphone access was denied. You can still type your question.", heardStatus: "Please review the words we heard before sending.", thinking: "Finding a simple explanation…", responseError: "We could not reach the local app. Check that it is running, then try again.", calculation: "Calculation", calculator: "Calculator", month: "months", amount: "Monthly amount (₹)", principal: "Deposit / loan amount (₹)", annualRate: "Annual interest rate (%)", assumedRate: "Assumed annual rate (%)", duration: "Duration (months)", continue: "Review values", confirmTitle: "Please check these values", confirm: "Calculate now", change: "Change values", calcError: "Please check the values and try again.", result: "Illustrative result", assumptions: "Assumptions", closed: "Conversation cleared. No messages are saved.", noHindiVoice: "No Hindi speech voice is available on this device; the written answer is shown.", noVoice: "Speech output is not available here; the written answer is shown.", calculationDisclaimer: "Illustrative estimate only. Actual products and outcomes may differ.", useText: "You can type your question below.", sensitive: "For your safety, never share OTP, UPI PIN, CVV, password, or banking credentials."
  },
  hi: {
    eyebrow: "पैसों की बात, आसान भाषा में", welcome: "पैसों से जुड़े सवाल,<br>आपकी अपनी भाषा में।", intro: "बचत, लोन या बीमा के बारे में पूछें। हम आसान भाषा में, एक-एक कदम समझाएँगे।", start: "शुरू करें", how: "आप क्या जानना चाहेंगे?", ask: "पूछें",
    voiceNotice: "आवाज़ आपके ब्राउज़र की स्पीच सेवा से समझी जाती है। आपके ब्राउज़र के अनुसार आवाज़ उसके सेवा प्रदाता तक जा सकती है। आप लिखकर भी पूछ सकते हैं।", tapSpeak: "बोलने के लिए दबाएँ", orType: "या लिखें", questionLabel: "आपका सवाल", ready: "जब चाहें शुरू करें। जवाब से पहले आपके शब्द यहाँ दिखेंगे।", heard: "हमने सुना:", edit: "बदलें", askThis: "यह पूछें", tryAsk: "ऐसे पूछें", yourAnswer: "आपका जवाब", listen: "सुनें", explore: "विषय चुनें", topics: "जो आपके लिए ज़रूरी है, वहाँ से शुरू करें", chooseCard: "जानने के लिए चुनें", banking: "बैंकिंग", bankingSub: "खाते और बुनियादी बातें", savings: "बचत", savingsSub: "कल के लिए योजना", loans: "लोन", loansSub: "लागत समझें", insurance: "बीमा", insuranceSub: "कवरेज जानें", tools: "आसान टूल", calculators: "कैलकुलेटर आज़माएँ", illustrative: "अनुमान और उनकी जानकारी", savingsCalc: "बचत", savingsCalcSub: "मासिक जमा जोड़ें", fdCalc: "फिक्स्ड डिपॉज़िट", fdCalcSub: "परिपक्वता और ब्याज का अनुमान", emiCalc: "EMI", emiCalcSub: "मासिक किस्त समझें", sipCalc: "SIP अनुमान", sipCalcSub: "एक उदाहरण देखें", safeTitle: "आपकी सुरक्षा सबसे पहले।", safeText: "हमें OTP, UPI PIN, पासवर्ड, CVV या बैंक विवरण की ज़रूरत नहीं। यह सीखने के लिए है, वित्तीय सलाह नहीं। अनुमान तय नहीं होते; रिटर्न की गारंटी नहीं।", clear: "बातचीत मिटाएँ", localNote: "पेज छोड़ने के बाद बातचीत सेव नहीं रहती।", listening: "सुन रहा है… अपना सवाल बोलें।", unsupported: "इस ब्राउज़र में आवाज़ पहचान उपलब्ध नहीं है। सवाल लिखें या नमूना चुनें।", noSpeech: "आवाज़ समझ नहीं आई। फिर कोशिश करें या सवाल लिखें।", micDenied: "माइक्रोफ़ोन की अनुमति नहीं मिली। आप सवाल लिख सकते हैं।", heardStatus: "भेजने से पहले पहचाने गए शब्द जाँचें।", thinking: "आसान जवाब ढूँढ रहे हैं…", responseError: "स्थानीय ऐप से संपर्क नहीं हुआ। ऐप चालू है या नहीं जाँचें और फिर कोशिश करें।", calculation: "गणना", calculator: "कैलकुलेटर", month: "महीने", amount: "हर महीने की रकम (₹)", principal: "जमा / लोन की रकम (₹)", annualRate: "सालाना ब्याज दर (%)", assumedRate: "मानी गई सालाना दर (%)", duration: "अवधि (महीने)", continue: "रकम जाँचें", confirmTitle: "कृपया रकम जाँचें", confirm: "अब गणना करें", change: "रकम बदलें", calcError: "रकम जाँचें और फिर कोशिश करें।", result: "अनुमानित नतीजा", assumptions: "मान्यताएँ", closed: "बातचीत मिटा दी गई। कोई संदेश सेव नहीं है।", noHindiVoice: "इस डिवाइस पर हिन्दी आवाज़ उपलब्ध नहीं है; लिखित जवाब देखें।", noVoice: "यहाँ आवाज़ उपलब्ध नहीं है; लिखित जवाब देखें।", calculationDisclaimer: "यह केवल अनुमान है। असली उत्पाद और परिणाम अलग हो सकते हैं।", useText: "आप नीचे सवाल लिख सकते हैं।", sensitive: "सुरक्षा के लिए OTP, UPI PIN, CVV, पासवर्ड या बैंक जानकारी साझा न करें।"
  }
};

const state = { language: "en", recognition: null, transcript: "", pendingCalculation: null, calculatorProgress: null, answer: "" };
const byId = (id) => document.getElementById(id);
const languagePicker = byId("language");
const questionInput = byId("question");
const statusText = byId("voice-status");

function setStatus(message) { statusText.textContent = message; }
function setLanguage(language) {
  state.language = language;
  document.documentElement.lang = language;
  const words = copy[language];
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const value = words[element.dataset.i18n];
    if (value) {
      if (element.dataset.i18n === "welcome") element.innerHTML = value;
      else element.textContent = value;
    }
  });
  languagePicker.value = language;
  loadExamples();
}

async function loadExamples() {
  const holder = byId("examples");
  holder.replaceChildren();
  try {
    const response = await fetch(`/api/examples?language=${state.language}`);
    const data = await response.json();
    data.examples.slice(0, 4).forEach((example) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "example-chip";
      button.textContent = example;
      button.addEventListener("click", () => { questionInput.value = example; submitQuestion(example); });
      holder.append(button);
    });
  } catch (_) {
    holder.textContent = copy[state.language].useText;
  }
}

async function submitQuestion(message) {
  const cleanMessage = String(message || "").trim();
  if (!cleanMessage) return;
  questionInput.value = cleanMessage;
  byId("transcript-review").hidden = true;
  setStatus(copy[state.language].thinking);
  try {
    const response = await fetch("/api/ask", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ message: cleanMessage, language: state.language }) });
    const result = await response.json();
    if (!response.ok) throw new Error(result.detail || "Request failed");
    state.answer = result.answer;
    byId("answer-text").textContent = result.answer;
    byId("answer-meta").textContent = result.intent === "safety" ? copy[state.language].sensitive : copy[state.language].calculationDisclaimer;
    byId("answer-panel").hidden = false;
    setStatus("");
    if (result.intent === "calculate" && calculatorInfo[result.topic]) openCalculator(result.topic);
    byId("answer-panel").scrollIntoView({ behavior: "smooth", block: "nearest" });
  } catch (_) {
    setStatus(copy[state.language].responseError);
  }
}

byId("ask-form").addEventListener("submit", (event) => { event.preventDefault(); submitQuestion(questionInput.value); });
byId("mic-button").addEventListener("click", () => {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) { setStatus(copy[state.language].unsupported); questionInput.focus(); return; }
  const recognition = new SpeechRecognition();
  state.recognition = recognition;
  recognition.lang = state.language === "hi" ? "hi-IN" : "en-IN";
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;
  recognition.onstart = () => { byId("mic-button").classList.add("listening"); setStatus(copy[state.language].listening); };
  recognition.onresult = (event) => {
    state.transcript = event.results[0][0].transcript;
    byId("transcript-text").textContent = state.transcript;
    byId("transcript-review").hidden = false;
    setStatus(copy[state.language].heardStatus);
  };
  recognition.onerror = (event) => {
    const message = event.error === "not-allowed" || event.error === "service-not-allowed" ? copy[state.language].micDenied : copy[state.language].noSpeech;
    setStatus(message);
  };
  recognition.onend = () => byId("mic-button").classList.remove("listening");
  try { recognition.start(); } catch (_) { setStatus(copy[state.language].noSpeech); }
});
byId("confirm-transcript").addEventListener("click", () => submitQuestion(state.transcript));
byId("edit-transcript").addEventListener("click", () => { questionInput.value = state.transcript; questionInput.focus(); });
byId("speak-answer").addEventListener("click", () => {
  if (!("speechSynthesis" in window)) { setStatus(copy[state.language].noVoice); return; }
  const utterance = new SpeechSynthesisUtterance(state.answer);
  utterance.lang = state.language === "hi" ? "hi-IN" : "en-IN";
  const voices = window.speechSynthesis.getVoices();
  const prefix = state.language === "hi" ? "hi" : "en";
  const voice = voices.find((item) => item.lang.toLowerCase().startsWith(prefix));
  if (state.language === "hi" && !voice) { setStatus(copy[state.language].noHindiVoice); return; }
  if (voice) utterance.voice = voice;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utterance);
});
languagePicker.addEventListener("change", (event) => setLanguage(event.target.value));

const categoryPrompts = {
  banking: { en: "How does a bank account work?", hi: "बैंक खाता कैसे काम करता है?" },
  savings: { en: "How can I start saving?", hi: "मैं बचत कैसे शुरू करूँ?" },
  loan: { en: "What should I understand before taking a loan?", hi: "लोन लेने से पहले क्या समझना चाहिए?" },
  insurance: { en: "How does insurance work?", hi: "बीमा कैसे काम करता है?" }
};
document.querySelectorAll(".topic-card").forEach((card) => card.addEventListener("click", () => submitQuestion(categoryPrompts[card.dataset.topic][state.language])));

const calculatorInfo = {
  savings: { title: "savingsCalc", fields: [{ key: "monthly_amount", label: "amount", min: "0.01", step: "0.01" }, { key: "months", label: "duration", min: "1", max: "600", step: "1" }] },
  fd: { title: "fdCalc", fields: [{ key: "principal", label: "principal", min: "0.01", step: "0.01" }, { key: "annual_rate_percent", label: "annualRate", min: "0", max: "100", step: "0.01" }, { key: "months", label: "duration", min: "1", max: "600", step: "1" }] },
  emi: { title: "emiCalc", fields: [{ key: "principal", label: "principal", min: "0.01", step: "0.01" }, { key: "annual_rate_percent", label: "annualRate", min: "0", max: "100", step: "0.01" }, { key: "months", label: "duration", min: "1", max: "600", step: "1" }] },
  sip: { title: "sipCalc", fields: [{ key: "monthly_amount", label: "amount", min: "0.01", step: "0.01" }, { key: "annual_assumed_rate_percent", label: "assumedRate", min: "0", max: "100", step: "0.01" }, { key: "months", label: "duration", min: "1", max: "600", step: "1" }] }
};

function openCalculator(kind) {
  state.pendingCalculation = null;
  state.calculatorProgress = { kind, values: {}, index: 0 };
  renderCalculatorStep();
}

function renderCalculatorStep() {
  const panel = byId("calculator-panel");
  const progress = state.calculatorProgress;
  if (!progress) return;
  const info = calculatorInfo[progress.kind];
  const field = info.fields[progress.index];
  const words = copy[state.language];
  const heading = document.createElement("h3"); heading.textContent = `${words.calculator}: ${words[info.title]}`;
  const intro = document.createElement("p"); intro.textContent = `${words["step"] || "Step"} ${progress.index + 1} ${words["of"] || "of"} ${info.fields.length} — ${words[field.label]}. ${words.calculationDisclaimer}`;
  const form = document.createElement("form"); form.className = "calc-form";
  const label = document.createElement("label"); label.textContent = words[field.label];
  const input = document.createElement("input"); input.name = field.key; input.type = "number"; input.required = true; input.min = field.min; input.step = field.step; input.inputMode = "decimal"; input.autofocus = true;
  if (field.max) input.max = field.max;
  label.append(input);
  const submit = document.createElement("button"); submit.type = "submit"; submit.textContent = progress.index === info.fields.length - 1 ? (words.review || words.continue) : words.continue;
  form.append(label, submit);
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const value = Number(input.value);
    if (!Number.isFinite(value) || value < Number(field.min) || (field.max && value > Number(field.max)) || (field.key === "months" && !Number.isInteger(value))) { setStatus(words.calcError); return; }
    progress.values[field.key] = value;
    progress.index += 1;
    if (progress.index < info.fields.length) renderCalculatorStep();
    else { state.pendingCalculation = { calculator: progress.kind, ...progress.values }; showConfirmation(); }
  });
  panel.replaceChildren(heading, intro, form);
  panel.hidden = false;
  panel.scrollIntoView({ behavior: "smooth", block: "center" });
  input.focus({ preventScroll: true });
}

function showConfirmation() {
  const panel = byId("calculator-panel");
  const words = copy[state.language];
  const box = document.createElement("div"); box.className = "confirm-box";
  const heading = document.createElement("h3"); heading.textContent = words.confirmTitle;
  const summary = document.createElement("p");
  const details = Object.entries(state.pendingCalculation).filter(([key]) => key !== "calculator").map(([key, value]) => {
    const known = { monthly_amount: words.amount, principal: words.principal, annual_rate_percent: words.annualRate, annual_assumed_rate_percent: words.assumedRate, months: words.duration };
    return `${known[key]}: ${value}`;
  });
  if ("speechSynthesis" in window) {
    const speechText = `${words.confirmTitle}. ${details.join(". ")}`;
    const utterance = new SpeechSynthesisUtterance(speechText);
    utterance.lang = state.language === "hi" ? "hi-IN" : "en-IN";
    const voice = window.speechSynthesis.getVoices().find((item) => item.lang.toLowerCase().startsWith(state.language === "hi" ? "hi" : "en"));
    if (voice) { utterance.voice = voice; window.speechSynthesis.cancel(); window.speechSynthesis.speak(utterance); }
  }
  summary.textContent = details.join(" · ");
  const buttons = document.createElement("div"); buttons.className = "confirm-actions";
  const yes = document.createElement("button"); yes.className = "confirm-yes"; yes.type = "button"; yes.textContent = words.confirm; yes.addEventListener("click", runCalculation);
  const no = document.createElement("button"); no.className = "confirm-no"; no.type = "button"; no.textContent = words.change; no.addEventListener("click", () => openCalculator(state.pendingCalculation.calculator));
  buttons.append(yes, no); box.append(heading, summary, buttons); panel.replaceChildren(box);
}

async function runCalculation() {
  const request = state.pendingCalculation;
  if (!request) return;
  const panel = byId("calculator-panel");
  try {
    const response = await fetch("/api/calculate", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(request) });
    const result = await response.json();
    if (!response.ok) throw new Error(result.detail || "Invalid values");
    const title = document.createElement("h3"); title.textContent = copy[state.language].result;
    const box = document.createElement("div"); box.className = "result-box";
    const primary = document.createElement("h4"); primary.textContent = result.monthly_emi !== undefined ? `Monthly EMI: ₹${result.monthly_emi.toLocaleString("en-IN")}` : result.maturity_value !== undefined ? `Maturity value: ₹${result.maturity_value.toLocaleString("en-IN")}` : result.estimated_value !== undefined ? `Estimated value: ₹${result.estimated_value.toLocaleString("en-IN")}` : `Total saved: ₹${result.total_saved.toLocaleString("en-IN")}`;
    const breakdown = document.createElement("p");
    if (result.total_payment !== undefined) breakdown.textContent = `Total payment: ₹${result.total_payment.toLocaleString("en-IN")} · Interest: ₹${result.total_interest.toLocaleString("en-IN")}`;
    else if (result.interest_earned !== undefined) breakdown.textContent = `Interest: ₹${result.interest_earned.toLocaleString("en-IN")}`;
    else if (result.total_contribution !== undefined) breakdown.textContent = `Contributions: ₹${result.total_contribution.toLocaleString("en-IN")}${result.estimated_growth !== undefined ? ` · Illustrative growth: ₹${result.estimated_growth.toLocaleString("en-IN")}` : ""}`;
    const assumptionsTitle = document.createElement("strong"); assumptionsTitle.textContent = copy[state.language].assumptions;
    const list = document.createElement("ul");
    result.assumptions.forEach((assumption) => { const item = document.createElement("li"); item.textContent = assumption; list.append(item); });
    box.append(primary, breakdown, assumptionsTitle, list); panel.replaceChildren(title, box);
    state.pendingCalculation = null;
  } catch (_) {
    const error = document.createElement("p"); error.textContent = copy[state.language].calcError; panel.append(error);
  }
}

document.querySelectorAll(".calculator-card").forEach((button) => button.addEventListener("click", () => openCalculator(button.dataset.calculator)));
byId("clear-button").addEventListener("click", () => {
  if (state.recognition) { try { state.recognition.abort(); } catch (_) {} }
  if ("speechSynthesis" in window) window.speechSynthesis.cancel();
  state.pendingCalculation = null; state.calculatorProgress = null; state.transcript = ""; state.answer = "";
  questionInput.value = ""; byId("answer-text").textContent = ""; byId("answer-meta").textContent = "";
  byId("answer-panel").hidden = true; byId("transcript-review").hidden = true; byId("calculator-panel").hidden = true;
  setStatus(copy[state.language].closed);
});

setLanguage("en");
