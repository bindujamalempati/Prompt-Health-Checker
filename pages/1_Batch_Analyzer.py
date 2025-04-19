
import streamlit as st
import pandas as pd
from detector.contextual_rules import smart_detect
import pdfplumber
import pytesseract
from PIL import Image
import tempfile
import re

st.title("📁 Multi-File Prompt Analyzer")

uploaded_file = st.file_uploader("Upload a CSV, PDF, or PNG file", type=["csv", "pdf", "png", "jpg", "jpeg"])

def analyze_prompt_list(prompts):
    results = []
    for prompt in prompts:
        risk, reason = smart_detect(prompt)
        results.append({
            "prompt": prompt,
            "risk_level": risk,
            "reason" : reason if reason else ""
        })
    return pd.DataFrame(results)

def highlight_text(text, keywords):
    if not keywords:
        return text
    for word in keywords:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub(f"**:red[\\g<0>]**", text)
    return text

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        if "prompt" not in df.columns:
            st.error("CSV must contain a 'prompt' column.")
        else:
            result_df = analyze_prompt_list(df["prompt"].tolist())
            st.dataframe(result_df)
            st.download_button("📥 Download CSV", result_df.to_csv(index=False), file_name="csv_results.csv")

    elif uploaded_file.name.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            all_prompts = []
            all_pages_text = []
            for page_num, page in enumerate(pdf.pages):
                extracted = page.extract_text()
                if extracted:
                    all_prompts.append(extracted)
                    all_pages_text.append(f"**Page {page_num + 1}:**\n" + extracted)
            result_df = analyze_prompt_list(all_prompts)
            risky = result_df[result_df["risk_level"] != "Low"]
            st.info(f"📊 {len(risky)} risky prompt(s) found across {len(all_prompts)} page(s).")
            st.dataframe(result_df)

            for i, row in result_df.iterrows():
                if row["risk_level"] != "Low":
                    keywords = row["reason"].split()
                    st.markdown(f"#### ⚠️ Risk in Page {i+1} — {row['risk_level']}")
                    st.markdown(highlight_text(all_prompts[i], keywords), unsafe_allow_html=True)

    elif uploaded_file.name.lower().endswith((".png", ".jpg", ".jpeg")):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            tmp_file.write(uploaded_file.read())
            img = Image.open(tmp_file.name)
            extracted_text = pytesseract.image_to_string(img)
            result_df = analyze_prompt_list([extracted_text])
            st.dataframe(result_df)
