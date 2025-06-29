import streamlit as st
from agents.fact_agent import verify_claim

st.set_page_config(page_title="Agentic Fact Verification System", layout="wide")
st.title("🕵️ Agentic Fact Verification System")
st.markdown("Enter a **claim** below and let the agent verify its authenticity using RAG and LLMs.")

# Input box
claim = st.text_area("🔎 Enter your factual claim here:", height=100)

# Button to trigger verification
if st.button("Verify Claim"):
    if claim.strip():
        with st.spinner("Verifying the claim... Please wait."):
            result = verify_claim(claim)
        st.success("Verification Complete!")
        st.markdown(f"### ✅ **Verdict**: `{result['verdict']}`")
        st.markdown(f"**Justification:** {result['justification']}")
        st.markdown("#### 🔗 Relevant Context:")
        for idx, context in enumerate(result['contexts'], 1):
            st.markdown(f"**[{idx}]** {context}")
    else:
        st.warning("Please enter a valid claim before submitting.")
