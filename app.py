
import streamlit as st
import cohere
from detector.contextual_rules import smart_detect

st.set_page_config(page_title="Prompt Health Checker", page_icon="🛡️")

debug_mode = st.sidebar.checkbox("🛠 Developer Mode (Show rule reason)")

def rewrite_prompt(prompt):
    try:
        co = cohere.Client(st.secrets["COHERE_API_KEY"])
        response = co.generate(
            model='command-light',
            prompt=f"Rewrite this prompt to remove bias, PII, or unsafe language: {prompt}",
            max_tokens=100,
            temperature=0.5
        )
        return response.generations[0].text.strip()
    except Exception:
        return None  # suppress errors gracefully

def fallback_safe_prompt(prompt):
    return "This prompt may contain unsafe or biased content. Consider rewording it to remove personal identifiers or sensitive topics."

st.title("🛡️ Prompt Health Checker")
prompt = st.text_area("Enter prompt to evaluate")

if st.button("Analyze Prompt"):
    level, reason = smart_detect(prompt)
    if level == "High":
        st.error("🚨 High Risk Detected")
    elif level == "Medium":
        st.warning("⚠️ Contextual Risk Detected")
    else:
        st.success("🟢 No major risks detected")

    if debug_mode and reason:
        st.info(f"Reason: {reason}")

    if level in ["High", "Medium"]:
        st.markdown("### ✨ Suggested Safe Prompt")
        safe_version = rewrite_prompt(prompt)
        if safe_version:
            st.text_area("✅ Try this version:", value=safe_version, height=100)
        else:
            st.warning("⚠️ Prompt rewrite service unavailable. Here is a basic suggestion:")
            st.text_area("✅ Try this version:", value=fallback_safe_prompt(prompt), height=100)
