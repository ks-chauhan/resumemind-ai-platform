import streamlit as st
import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

from components.ai_assistant import render_ai_assistant, set_page_context

def main():
    st.set_page_config(
        page_title="ResumeMind - Resume Analysis AI Platform",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Set Page context for AI assistant
    set_page_context("home")

    # Render AI Assistant in Sidebar
    render_ai_assistant()

    # Main Page content
    st.title("ResumeMind - Resume Analysis AI Platform")
    st.markdown("### Transform Your Hiring Process with AI-Powered Resume Intelligence")

    # Introduction
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        **ResumeMind** leverages cutting-edge AI technology to revolutionize recruitment:
        - **RAG-powered analysis** for deep resume understanding
        - **Vector similarity matching** for precise job-candidate alignment  
        - **Fine-tuned language models** for domain-specific insights
        - **Intelligent scoring algorithms** for objective candidate evaluation
        """)
        
        # Feature overview
        st.markdown("---")
        st.subheader("🚀 Core Features")
        
        feature_col1, feature_col2 = st.columns(2)
        
        with feature_col1:
            st.markdown("""
            **🎯 Resume Scoring**
            - General resume quality assessment
            - Job-specific compatibility scoring
            - AI-powered improvement suggestions
            - Detailed skills analysis
            """)
        
        with feature_col2:
            st.markdown("""
            **🔍 Resume Shortlisting**  
            - Bulk resume processing
            - Automated candidate ranking
            - Customizable filtering criteria
            - Export shortlisted candidates
            """)
    
    with col2:
        st.markdown("### 🛠️ Technology Stack")
        st.markdown("""
        **AI/ML Frameworks:**
        - LangChain & LlamaIndex
        - Hugging Face Transformers
        - Sentence Transformers
        
        **Vector Databases:**
        - ChromaDB (Development)
        - Pinecone (Production)
        
        **Backend:**
        - FastAPI & Uvicorn
        - PyTorch for ML
        
        **Frontend:**
        - Streamlit Dashboard
        """)
    
    # Getting Started
    st.markdown("---")
    st.subheader("🎯 Getting Started")
    st.markdown("""
    1. **📄 Upload resumes** in PDF or DOCX format
    2. **📋 Provide job descriptions** via file upload or text input  
    3. **⚡ Get instant AI analysis** with detailed scoring and insights
    4. **💬 Use the AI assistant** in the sidebar for guidance and tips
    """)
    
    # Navigation instructions
    st.info("👈 **Use the sidebar** to navigate between features and chat with the AI Assistant!")

if __name__ == "__main__":
    main()