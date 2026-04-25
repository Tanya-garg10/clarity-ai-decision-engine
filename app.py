import streamlit as st
import google.generativeai as genai
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Clarity AI – Smart Decision Engine",
    page_icon="🧠",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Custom CSS – minimal, modern look
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Global */
    .block-container { max-width: 760px; padding-top: 2rem; }

    /* Hero */
    .hero { text-align: center; margin-bottom: 1.5rem; }
    .hero h1 { font-size: 2.2rem; margin-bottom: 0.2rem; }
    .hero p  { color: #888; font-size: 1.05rem; }

    /* Section cards */
    .section-card {
        background: rgba(128, 128, 128, 0.1);
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #4f8cff;
        color: inherit;
    }
    .section-card h3 { margin-top: 0; color: inherit; }
    .section-card p  { color: inherit; }

    .card-risk   { border-left-color: #ff6b6b; }
    .card-rec    { border-left-color: #51cf66; }
    .card-conf   { border-left-color: #fcc419; }
    .card-insight{ border-left-color: #845ef7; }

    /* Confidence badge */
    .conf-badge {
        display: inline-block;
        font-size: 2rem;
        font-weight: 700;
        color: #4f8cff;
    }

    /* Option columns */
    .pro  { color: #2b8a3e; }
    .con  { color: #c92a2a; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="hero">'
    "<h1>🧠 Clarity AI</h1>"
    "<p>Smart Decision Engine — powered by Google Gemini</p>"
    "</div>",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Gemini prompt builder
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """You are Clarity AI, an expert decision-analysis assistant.

Given a real-life situation from the user, return a **structured JSON** object with
exactly these keys (no markdown, no extra text — only valid JSON):

{
  "situation_breakdown": "A clear, concise summary of the situation and its core tension.",
  "options": [
    {
      "name": "Option name",
      "pros": ["pro 1", "pro 2"],
      "cons": ["con 1", "con 2"]
    }
  ],
  "risks": ["risk 1", "risk 2", "risk 3"],
  "key_insight": "One powerful, non-obvious insight the user should consider.",
  "recommendation": "Your recommended course of action with brief reasoning.",
  "confidence_percent": 82
}

Rules:
- Provide 2-4 realistic options.
- Each option must have at least 2 pros and 2 cons.
- List 2-5 concrete risks.
- confidence_percent is an integer 0-100 reflecting how confident you are in the recommendation.
- Be empathetic, practical, and balanced.
- Output ONLY the JSON object — no markdown fences, no commentary.
"""


def build_prompt(user_input: str) -> str:
    return f"{SYSTEM_PROMPT}\n\nUser situation:\n{user_input}"


# ---------------------------------------------------------------------------
# Gemini call
# ---------------------------------------------------------------------------
def call_gemini(user_input: str, api_key: str) -> dict:
    """Send the situation to Gemini and return parsed JSON."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(
        build_prompt(user_input),
        generation_config=genai.GenerationConfig(temperature=0.7),
    )
    text = response.text.strip()
    # Strip markdown fences if the model wraps them anyway
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


# ---------------------------------------------------------------------------
# Render helpers
# ---------------------------------------------------------------------------
def render_section(title: str, body: str, css_class: str = ""):
    cls = f"section-card {css_class}".strip()
    st.markdown(
        f'<div class="{cls}"><h3>{title}</h3><p>{body}</p></div>',
        unsafe_allow_html=True,
    )


def render_options(options: list):
    for opt in options:
        with st.expander(f"📌 {opt['name']}", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**✅ Pros**")
                for p in opt.get("pros", []):
                    st.markdown(f'<span class="pro">• {p}</span>', unsafe_allow_html=True)
            with col2:
                st.markdown("**❌ Cons**")
                for c in opt.get("cons", []):
                    st.markdown(f'<span class="con">• {c}</span>', unsafe_allow_html=True)


def render_risks(risks: list):
    items = "".join(f"<li>{r}</li>" for r in risks)
    st.markdown(
        f'<div class="section-card card-risk"><h3>⚠️ Risks</h3><ul>{items}</ul></div>',
        unsafe_allow_html=True,
    )


def render_confidence(pct: int):
    st.markdown(
        f'<div class="section-card card-conf">'
        f'<h3>📊 Confidence</h3>'
        f'<span class="conf-badge">{pct}%</span>'
        f"</div>",
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------------------
# Sidebar – API key & sample inputs
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        value=os.getenv("GEMINI_API_KEY", ""),
        help="Get a free key at https://aistudio.google.com/app/apikey",
    )
    st.divider()
    st.subheader("💡 Sample Inputs")
    samples = {
        "Career": (
            "I'm a mid-level software engineer with 5 years of experience. "
            "I've received a job offer from a startup that pays 20% more but has "
            "no job security. My current company is stable but growth is slow. "
            "I also have an idea for my own SaaS product. What should I do?"
        ),
        "Financial": (
            "I have $30,000 in savings. I can either invest in an index fund, "
            "put a down payment on a rental property, or pay off my student loans "
            "which have a 5.5% interest rate. I'm 28 and single with no dependents."
        ),
        "Personal": (
            "I've been offered a chance to move abroad for 2 years for work. "
            "My partner has a stable job here and we just adopted a dog. "
            "The opportunity would double my salary and boost my career, "
            "but I'm worried about the relationship and settling in a new country."
        ),
    }
    for label, text in samples.items():
        if st.button(f"Try: {label} decision", use_container_width=True):
            st.session_state["sample_input"] = text

# ---------------------------------------------------------------------------
# Main input area
# ---------------------------------------------------------------------------
default_text = st.session_state.pop("sample_input", "")
situation = st.text_area(
    "Describe your situation",
    value=default_text,
    height=160,
    placeholder="e.g. I'm deciding between two job offers…",
)

analyze = st.button("🔍 Analyze", type="primary", use_container_width=True)

# ---------------------------------------------------------------------------
# Run analysis
# ---------------------------------------------------------------------------
if analyze:
    if not api_key:
        st.error("Please enter your Gemini API key in the sidebar.")
    elif not situation.strip():
        st.warning("Please describe a situation first.")
    else:
        with st.spinner("Thinking deeply about your situation…"):
            try:
                result = call_gemini(situation, api_key)
            except json.JSONDecodeError:
                st.error("Gemini returned an unexpected format. Please try again.")
                st.stop()
            except Exception as exc:
                st.error(f"API error: {exc}")
                st.stop()

        st.success("Analysis complete!")

        # Situation Breakdown
        render_section("📋 Situation Breakdown", result.get("situation_breakdown", ""))

        # Options
        st.markdown("### 🔀 Options")
        render_options(result.get("options", []))

        # Risks
        render_risks(result.get("risks", []))

        # Key Insight
        render_section(
            "💡 Key Insight",
            result.get("key_insight", ""),
            css_class="card-insight",
        )

        # Recommendation
        render_section(
            "✅ Recommendation",
            result.get("recommendation", ""),
            css_class="card-rec",
        )

        # Confidence
        render_confidence(result.get("confidence_percent", 0))

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption("Built with ❤️ using Streamlit & Google Gemini · Clarity AI © 2026")
