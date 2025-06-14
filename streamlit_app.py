import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Awesome LLM Apps", layout="wide")

st.title("Awesome LLM Apps")

readme = Path("README.md").read_text()

st.markdown(readme)
