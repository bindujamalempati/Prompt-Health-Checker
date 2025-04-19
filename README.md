

### 📄 `README.md` — Prompt Health Checker

```markdown
# 🛡️ Prompt Health Checker

**Prompt Health Checker** is an intelligent LLM safety tool that evaluates user-entered prompts for **privacy**, **bias**, **toxicity**, and **prompt injection** risks. It generates safe alternatives using Cohere and flags risky language using smart rule-based and contextual detection.

> ⚡ Built for AI developers, enterprise compliance teams, researchers, and safety-first LLM startups.

---

## 🚀 Features

- 🔍 **Multi-Risk Detection**  
  Identifies PII exposure, gender bias, prompt injection, and offensive content.

- ✨ **Safe Prompt Rewriter**  
  Rewrites unsafe prompts using [Cohere API](https://cohere.ai).

- 🧠 **Smart Rule Matching**  
  Context-aware detection (e.g., “brutal attack” vs “brutal workout”).

- 📊 **Risk Levels**  
  Flags prompts as `Low`, `Medium`, or `High` risk with explanations.

- 🧪 **Developer Mode**  
  Shows matched rules and explanations (toggleable via sidebar).

- 📁 **Batch Analyzer**  
  Upload CSV, PDF, or PNG files and auto-analyze all prompts.

- 📥 **Report Export**  
  Download result summaries in CSV format.

- 🖥️ **Streamlit UI**  
  Clean, interactive UI for tech and non-tech users.

---

## 🧑‍💻 Technologies Used

| Stack Layer       | Tools / Libraries                                  |
|-------------------|----------------------------------------------------|
| UI                | [Streamlit](https://streamlit.io)                  |
| NLP & Rewrite     | [Cohere API](https://cohere.ai)                    |
| File Processing   | `pdfplumber`, `pytesseract`, `Pillow`, `pandas`    |
| Detection Engine  | `regex`, contextual keyword rules, rule explanations |
| Deployment Ready  | GitHub, Streamlit Cloud compatible                 |

---

## 🎯 Who Will Benefit?

| User Type               | Benefit                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| 🔐 LLM Developers        | Test prompts before passing to models like GPT, Claude, Cohere.         |
| 🏢 Enterprise Teams      | Ensure prompts don't leak sensitive or biased data.                     |
| 🧪 Researchers           | Analyze how humans or LLMs phrase potentially unsafe inputs.            |
| 🗂️ Product Managers      | Deploy pre-validation tools for user-submitted prompts.                 |
| 🧑‍🎓 Students/Learners    | Learn prompt engineering, AI ethics, and NLP guardrails.                |

---

## 🛠️ How to Run Locally

### 1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/prompt-health-checker.git
cd prompt-health-checker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Cohere API key

Edit `.streamlit/secrets.toml`:

```toml
COHERE_API_KEY = "your_actual_cohere_key"
```

> 🔑 Get your API key at https://dashboard.cohere.com

### 4. Run the app

```bash
streamlit run app.py
```

---







### ✅ What to Do Next:

1. Create a file in your project: `README.md`
2. Copy-paste the content above
3. Commit and push:

```bash
git add README.md
git commit -m "Add project README"
git push
```

---
