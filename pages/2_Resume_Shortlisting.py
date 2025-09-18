import streamlit as st
import sys
from pathlib import Path

# Add src to the path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from components.ai_assistant import render_ai_assistant, set_page_context

st.set_page_config(page_title="Resume Shortlisting")

# Set Page Context for AI Assistant
set_page_context("resume_shortlisting")

# Render AI Assistant in the sidebar
render_ai_assistant()

st.title("Resume Shortlisting System")
st.markdown("Effectively rank and filter multiple candidates for any position")

# Add AI helper tips
st.sidebar.markdown("---")
st.sidebar.info("💡 **AI Tip:** Ask the AI Assistant about optimal shortlisting strategies and filtering criteria!")