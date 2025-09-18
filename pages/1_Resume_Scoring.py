import streamlit as st
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from components.ai_assistant import render_ai_assistant, set_page_context

st.set_page_config(page_title="Resume Scoring")

# Set page context for AI assistant
set_page_context("resume_scoring")

# Render AI Assistant in sidebar
render_ai_assistant()

st.title("🎯 Resume Scoring & Analysis")
st.markdown("**Comprehensive AI-powered resume evaluation and job matching**")

# Rest of your existing Resume Scoring code...
# (Keep all the existing functionality)

# Add AI helper tips in main content
st.sidebar.markdown("---")
st.sidebar.info("💡 **AI Tip:** Ask the AI Assistant about scoring weights and evaluation criteria while you work!")
