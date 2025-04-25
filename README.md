

# 🛡️ Prompt Health Checker

**Prompt Health Checker** is a smart LLM safety tool designed to evaluate user-entered prompts for **privacy risks**, **bias**, **toxicity**, and **prompt injection** vulnerabilities. It not only flags risky content but also **suggests safer alternatives** using the Cohere API, making it an essential tool for AI practitioners, enterprises, and researchers focused on safe AI deployment.

> ⚡ Built for AI developers, compliance teams, safety researchers, and LLM-driven startups.

---

## 🚀 Features

- 🔍 **Multi-Risk Detection**  
  Detects personally identifiable information (PII), gender or racial bias, toxic language, and prompt injection attempts.

- ✨ **Safe Prompt Rewriter**  
  Automatically rewrites unsafe prompts to safer alternatives using [Cohere's NLP capabilities](https://cohere.ai).

- 🧠 **Context-Aware Rule Matching**  
  Understands context to differentiate between benign and harmful uses of language.

- 📊 **Risk Level Classification**  
  Categorizes each prompt into `Low`, `Medium`, or `High` risk, along with explanations.

- 🧪 **Developer Mode**  
  Optional mode to reveal matched rules, detection reasons, and internal insights.

- 📁 **Batch File Analysis**  
  Upload `.csv`, `.pdf`, or `.png` files to bulk-analyze multiple prompts at once.

- 📥 **Export Reports**  
  Download prompt analysis summaries as `.csv` reports.

- 🖥️ **Interactive Streamlit UI**  
  Modern, user-friendly interface designed for both technical and non-technical users.

---

## 🧑‍💻 Technologies Used

| Layer                | Tools / Libraries                                |
|----------------------|--------------------------------------------------|
| Frontend UI          | [Streamlit](https://streamlit.io)                |
| NLP / Rewrite Engine | [Cohere API](https://cohere.ai)                  |
| File Handling        | `pdfplumber`, `pytesseract`, `Pillow`, `pandas`  |
| Risk Detection       | `regex` patterns, keyword rules, context matching |
| Hosting Ready        | GitHub, Streamlit Cloud                         |

---

## 🎯 Ideal Users

| Audience                | Purpose                                              |
|--------------------------|------------------------------------------------------|
| 🔐 LLM Developers         | Pre-scan prompts before model inference.             |
| 🏢 Compliance Teams       | Verify prompt safety and prevent data leaks.         |
| 🧪 AI Ethics Researchers  | Study human and AI-generated unsafe phrasing.        |
| 🗂️ Product Managers       | Integrate into AI-driven applications' validation steps. |
| 🧑‍🎓 Students / Learners   | Understand prompt safety and AI content moderation. |

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/prompt-health-checker.git
cd prompt-health-checker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your Cohere API key

Create a `.streamlit/secrets.toml` file and add:

```toml
COHERE_API_KEY = "your_actual_cohere_api_key"
```

> 🔑 You can get your Cohere API key by signing up at [Cohere Dashboard](https://dashboard.cohere.com).

### 4. Launch the app

```bash
streamlit run app.py
```

---

## 📄 Example Usage

- Type or upload prompts into the UI.
- View risk scores (`Low`, `Medium`, `High`).
- Check why a prompt was flagged.
- Let the tool suggest a safer version of your prompt.
- Export the analysis report if needed!

---

## 📢 Contributing

I welcome contributions to improve the detection rules, UI/UX, and rewriting engine. Please submit a pull request or open an issue to discuss your ideas.

---



# 📬 Contact

For questions, feature requests, or feedback, reach out at:

- 📧 Email: malempatibinduja54@gmail.com


---

