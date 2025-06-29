# 🕵️ Agentic Fact Verification System

An interactive Streamlit-based application that uses Retrieval-Augmented Generation (RAG) and Google Gemini 1.5 Flash to **verify factual claims**. Built with an agentic architecture using CrewAI, this project fetches relevant context from Wikipedia and evaluates the claim using a multi-step reasoning pipeline.

---

## 🚀 Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agentic-fact-verification-system-3yqwkdmsz6jwtdbsvwixnq.streamlit.app/)



---

## 📂 Project Structure

```
agentic-fact-verification-system/
│
├── app.py                         # Streamlit UI
├── pipeline.py                   # End-to-end pipeline logic
│
├── agents/
│   ├── __init__.py
│   └── fact_agent.py             # Core agent logic
│
├── utils/
│   ├── __init__.py
│   ├── llm_utils.py              # Google Gemini LLM interaction
│   └── retrieval_utils.py        # Wikipedia search and retrieval
│
├── .env                          # Stores Gemini API Key
├── requirements.txt              # All required Python dependencies
└── README.md                     # You are here
```

---

## ⚙️ Tech Stack

- **Frontend**: Streamlit  
- **LLM**: Google Gemini 1.5 Flash  
- **Retrieval**: Wikipedia (via `wikipedia` Python package)  
- **Agent Framework**: CrewAI  
- **Environment**: python-dotenv  
- **Language**: Python 3.10

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## 🛠️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/ptanya3022/agentic-fact-verification-system.git
cd agentic-fact-verification-system

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

## 💡 How It Works

1. **Enter a factual claim** in the Streamlit UI.  
2. The agent **retrieves context** using a Wikipedia search.  
3. The Gemini LLM is prompted with the claim and context.  
4. The system **verifies** whether the claim is likely true or false with a justification.

---

## 📌 Example

> **Claim**: "Cows can fly."

🔍 **Verdict**: False  
📝 **Justification**: Cows are large, domesticated animals with no flight capability.  
📚 **Context**: Pulled from Wikipedia articles about cows.

---

## 🧠 Future Enhancements

- Add support for multiple LLMs (e.g., Claude, Mistral)  
- Add PDF/document context retrieval  
- Integrate long-term memory with FAISS or Chroma  
- Improve agentic planning with multi-step toolchains


