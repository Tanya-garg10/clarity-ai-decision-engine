# 🧠 Clarity AI – Smart Decision Engine

A hackathon-ready web app that uses **Google Gemini** to analyze real-life decisions (career, financial, personal) and return structured, actionable insights.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5--flash-yellow)

---

## ✨ Features

- **Structured Decision Analysis** – situation breakdown, options with pros/cons, risks, key insight, recommendation, and confidence score
- **Google Gemini Integration** – prompt-engineered for consistent JSON output
- **Clean UI** – card-based layout with color-coded sections
- **Sample Inputs** – one-click examples for career, financial, and personal decisions
- **Zero Config** – just add your API key and run

---

## 🚀 Quick Start

### 1. Clone & install

```bash
git clone https://github.com/Tanya-garg10/clarity-ai-decision-engine.git
cd clarity-ai-decision-engine
pip install -r requirements.txt
```

### 2. Add your Gemini API key

Get a free key at <https://aistudio.google.com/app/apikey>, then either:

- Create a `.env` file (copy from the example):
  ```bash
  cp .env.example .env
  # edit .env and paste your key
  ```
- Or paste it directly in the app sidebar.

### 3. Run

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## 📂 Project Structure

```
clarity-ai-decision-engine/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── sample_inputs.md    # Test scenarios for demo
└── README.md           # This file
```

---

## 🧪 Sample Test Inputs

See [sample_inputs.md](sample_inputs.md) for ready-to-paste scenarios covering career, financial, and personal decisions.

---

## 🛠️ How It Works

1. User types a real-life situation into the text box.
2. The app sends a prompt-engineered request to **Gemini 2.5 Flash**.
3. Gemini returns a structured JSON response.
4. Streamlit renders the analysis in color-coded cards.

---

## 🙌 Built With

- [Streamlit](https://streamlit.io/) – UI framework
- [Google Gemini API](https://ai.google.dev/) – AI intelligence
- [Python](https://www.python.org/) – backend language

---

<p align="center">Made with ❤️ for hackathons</p>
