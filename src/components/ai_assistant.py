import streamlit as st
def render_ai_assistant():
    """Render the AI Assistant in the Sidebar."""

    # Initialize Char history in session state
    if "ai_messages" not in st.session_state:
        st.session_state.ai_messages = [
            {
                "rola": "assistant",
                "content": "AI Assistant at your service! How can I help you today?"
            }
        ]
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### AI Assistant")

    # Show/hide chat
    if "show_ai_chat" not in st.session_state:
        st.session_state.show_ai_chat = False
    
    # Toggle button
    if st.sidebar.button("Toggle AI Chat", key = "ai_toggle"):
        st.session_state.show_ai_chat = not st.session_state.show_ai_chat
    
    if st.session_state.show_ai_chat:
        # Chat container in sidebar
        chat_container = st.sidebar.container()

        with chat_container:
            st.markdown("Recent Conversations:")

            # Show Recent messages
            recent_messages = st.session_state.ai_messages[-4:]
            for message in recent_messages:
                st.markdown(f" {message['content'][:100]}{"..." if len(message['content'])>100 else ""}")
            
            # Chat Input
            user_input = st.text_input("Ask AI Assistant:",
                                       key = "ai_input",
                                       placeholder = "Type your message here...")
            
            col1, col2 = st.columns([1, 1])

            with col1:
                if st.button("Send", key="AI_send"):
                    if user_input.strip():
                        # Add User message
                        st.session_state.ai_messages.append({
                            "role": "user",
                            "content": user_input
                        })
                        
                        # Generate AI response
                        response = generate_contextual_response(user_input)
                        st.session_state.ai_messages.append({
                            "role": "assistant",
                            "content": response
                        })

                        st.rerun()

            with col2:
                if st.button("Clear", key = "ai_clear"):
                    st.session_state.ai_messages = [
                        {
                            "role": "assistant",
                            "content": "Chat Cleared! How can i help you"
                        }
                    ]
                    st.rerun()
        
        # Quick help buttons

        if st.sidebar.button("Scoring Tips", key="quick_scoring"):
            add_quick_response("How should I score resumes effectively?")
        
        if st.sidebar.button("Shortlisting", key="quick_shortlist"):
            add_quick_response("What are best practices for shortlisting candidates?")
        
        if st.sidebar.button("Resume Analysis", key="quick_analysis"):
            add_quick_response("How do I analyze resume quality?")
        
    else:
        st.sidebar.markdown("*Click Above to chat with AI Assistant*")

        # Show Quick stats
        messages_count = len(st.session_state.ai_messages) - 1 # Exclude the initial message
        if messages_count > 0:
            st.sidebar.markdown("**{messages_count}** message in current session")
        
def add_quick_response(question):
    """Add Quick response to chat"""
    st.session_state.ai_messages.append({
        "role":"user",
        "content":question
    })
    response = generate_contextual_response(question)
    st.session_state.ai_messages.append({
        "role":"assisstant",
        "content":response
    })
    st.rerun()

def generate_contextual_response(prompt):
    """Generate Contextual AI responses based on current page and prompt"""

    # Get Current Page context
    current_page = st.session_state.get("current_page", "general")
    prompt_lower = prompt.lower()

    # Context Aware responses based on current page
    if "scoring" in current_page.lower() or any(word in prompt_lower for word in ["score", "rating", "evaluate"]):
        return generate_scoring_response(prompt_lower)
    elif "shortlist" in current_page.lower() or any(word in prompt_lower for word in ["shortlist", "filter", "rank"]):
        return generate_shortlisting_response(prompt_lower)
    else:
        return generate_general_response(prompt_lower)

def generate_scoring_response(prompt):
    """Generate scoring-specific responses"""
    if "weight" in prompt or "importance" in prompt:
        return """
        🎯 **Scoring Weight Guidelines:**
        
        **For Technical Roles:**
        - Skills: 45-50%
        - Experience: 30-35% 
        - Education: 15-20%
        
        **For Management Roles:**
        - Experience: 40-45%
        - Skills: 30-35%
        - Education: 20-25%
        
        💡 **Tip:** Adjust weights based on role criticality and team needs!
        """
    elif "improve" in prompt or "better" in prompt:
        return """
        📈 **Improve Scoring Accuracy:**
        
        ✅ **Best Practices:**
        - Use consistent criteria for all candidates
        - Score blind (remove names/photos initially)
        - Focus on achievements over responsibilities
        - Quantify impact when possible
        
        🎯 **Quick Checks:**
        - Are requirements clearly defined?
        - Do weights add up to 100%?
        - Is scoring rubric documented?
        """
    else:
        return """
        📊 **Resume Scoring Essentials:**
        
        **Key Areas to Evaluate:**
        🔹 **Skills Match** - Technical & soft skills alignment
        🔹 **Experience Depth** - Relevant role experience
        🔹 **Achievement Quality** - Quantified results
        🔹 **Growth Trajectory** - Career progression
        
        Need specific scoring advice? Ask about weights, criteria, or improvement tips!
        """

def generate_shortlisting_response(prompt):
    """Generate shortlisting-specific responses"""
    if "how many" in prompt or "number" in prompt:
        return """
        🔢 **Optimal Shortlisting Numbers:**
        
        **General Guidelines:**
        - **Initial Screen:** Top 20-30% of applicants
        - **Detailed Review:** 8-12 candidates  
        - **Phone/Video Screen:** 5-8 candidates
        - **Final Interviews:** 3-5 candidates
        
        **Factors to Consider:**
        - Role urgency and criticality
        - Interview capacity and time
        - Quality of applicant pool
        
        💡 **Pro Tip:** Quality over quantity - better to interview 3 great candidates than 8 mediocre ones!
        """
    elif "filter" in prompt or "criteria" in prompt:
        return """
        🔍 **Smart Filtering Criteria:**
        
        **Tier 1 (Must-Haves):**
        - Required education/certifications
        - Critical technical skills
        - Minimum experience threshold
        
        **Tier 2 (Preferred):**
        - Industry experience
        - Specific tool knowledge
        - Cultural fit indicators
        
        **Tier 3 (Nice-to-Have):**
        - Additional languages
        - Leadership experience
        - Advanced certifications
        
        Start with Tier 1, then add Tier 2/3 based on candidate pool size.
        """
    else:
        return """
        🎯 **Shortlisting Strategy:**
        
        **3-Stage Process:**
        
        **Stage 1:** Automated filtering
        - Keyword matching
        - Basic requirements check
        - Initial AI scoring
        
        **Stage 2:** Human review
        - Detailed resume analysis
        - Context evaluation
        - Cultural fit assessment
        
        **Stage 3:** Final selection
        - Comparative ranking
        - Diversity considerations
        - Interview scheduling
        
        Which stage do you need help with?
        """

def generate_general_response(prompt):
    """Generate general HR/recruitment responses"""
    if "bias" in prompt or "fair" in prompt:
        return """
        ⚖️ **Reducing Hiring Bias:**
        
        **Common Biases:**
        - Affinity bias (similar backgrounds)
        - Halo effect (one trait overshadows others)
        - Confirmation bias (seeking confirming info)
        
        **Mitigation Strategies:**
        ✅ Structured interviews
        ✅ Diverse interview panels  
        ✅ Blind resume reviews initially
        ✅ Standardized scoring rubrics
        ✅ Focus on job-relevant criteria only
        
        **Tools to Help:**
        - Remove names/photos for initial screening
        - Use consistent questions for all candidates
        - Document decision rationale
        """
    elif "interview" in prompt:
        return """
        🎤 **Interview Best Practices:**
        
        **Preparation:**
        - Review resume thoroughly
        - Prepare role-specific questions
        - Set clear evaluation criteria
        
        **Structure:**
        - Opening (5 min): Role overview
        - Technical (20 min): Skills assessment
        - Behavioral (15 min): STAR method
        - Cultural (10 min): Team fit
        - Closing (10 min): Candidate questions
        
        **Key Questions:**
        - "Walk me through your approach to..."
        - "Describe a time when you..."
        - "How would you handle..."
        """
    else:
        return """
        💡 **I'm here to help with recruitment!**
        
        **Ask me about:**
        📊 Resume scoring & evaluation
        🔍 Candidate shortlisting strategies
        🎤 Interview best practices
        ⚖️ Fair hiring & bias reduction
        📈 Process improvement tips
        
        **Current Context:** I can see you're working on resume analysis. Need specific help with scoring, filtering, or evaluation techniques?
        
        Just ask - I'm designed to give practical, actionable advice!
        """

# Page context tracking
def set_page_context(page_name):
    """Set current page context for AI assistant"""
    st.session_state.current_page = page_name