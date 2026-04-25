# 🧠 Clarity AI – Smart Decision Engine

A hackathon-ready web app that uses **Google Gemini** to analyze real-life decisions (career, financial, personal) and return structured, actionable insights.

&nbsp;

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5--flash-yellow)

&nbsp;

---

&nbsp;

## ✨ Features

&nbsp;

- **Structured Decision Analysis** – situation breakdown, options with pros/cons, risks, key insight, recommendation, and confidence score

- **Google Gemini Integration** – prompt-engineered for consistent JSON output

- **Clean UI** – card-based layout with color-coded sections

- **Sample Inputs** – one-click examples for career, financial, and personal decisions

- **Zero Config** – just add your API key and run

&nbsp;

---

&nbsp;

## 🚀 Quick Start

&nbsp;

### 1. Clone & install

```bash
git clone https://github.com/Tanya-garg10/clarity-ai-decision-engine.git
cd clarity-ai-decision-engine
pip install -r requirements.txt
```

&nbsp;

### 2. Add your Gemini API key

Get a free key at <https://aistudio.google.com/app/apikey>, then either:

- Create a `.env` file (copy from the example):
  ```bash
  cp .env.example .env
  # edit .env and paste your key
  ```
- Or paste it directly in the app sidebar.

&nbsp;

### 3. Run

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

&nbsp;

---

&nbsp;

## 📂 Project Structure

```
clarity-ai-decision-engine/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── sample_inputs.md    # Test scenarios for demo
└── README.md           # This file
```

&nbsp;

---

&nbsp;

## 🧪 Sample Test Inputs

See [sample_inputs.md](sample_inputs.md) for ready-to-paste scenarios covering career, financial, and personal decisions.

&nbsp;

---

&nbsp;

## 🛠️ How It Works

&nbsp;

1. User types a real-life situation into the text box.
2. The app sends a prompt-engineered request to **Gemini 2.5 Flash**.
3. Gemini returns a structured JSON response.
4. Streamlit renders the analysis in color-coded cards.

&nbsp;

---

&nbsp;

## 🛡️ License

Distributed under the **MIT License**. See below for details.

```
MIT License

Copyright (c) 2026 Tanya Garg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

&nbsp;

---

&nbsp;

## 🙌 Built With

- [Streamlit](https://streamlit.io/) – UI framework
- [Google Gemini API](https://ai.google.dev/) – AI intelligence
- [Python](https://www.python.org/) – backend language

&nbsp;

---

<p align="center">Made with ❤️ for hackathons</p>
