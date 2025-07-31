import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Load knowledge context
with open("slides_summary.txt", "r", encoding="utf-8") as f:
    context = f.read()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# Streamlit UI
st.set_page_config(page_title="LinkedIn Niche Selector", layout="centered")
st.title("🔍 LinkedIn Niche Selector")
st.markdown("Answer a few reflective questions to receive **your top 3 LinkedIn content niche recommendations** with useful links and top creators in each niche.")

with st.form("niche_form"):
    q1 = st.text_input("🧠 What are you good at or known for?")
    q2 = st.text_input("❤️ What topics do you genuinely enjoy discussing or exploring?")
    q3 = st.text_input("🎯 Who is your ideal LinkedIn audience?")
    q4 = st.selectbox("🚀 What kind of creator do you want to be?", ["Lifestyle-focused", "Performance-driven", "Somewhere in-between"])
    q5 = st.text_area("💡 What lessons, tools, or experiences could you teach others?", height=100)
    submitted = st.form_submit_button("Suggest My Niche")

if submitted:
    if not all([q1, q2, q3, q4, q5]):
        st.warning("Please answer all questions.")
    else:
        with st.spinner("🔍 Analyzing and generating your niche recommendations..."):
            prompt = f"""
            You are a top-tier LinkedIn content strategist, audience psychologist, and positioning expert. You help individuals craft a niche that aligns with their personal edge, market opportunity, and audience resonance — with clarity, creativity, and long-term growth in mind.

            Below are the user's responses to a reflective self-assessment. Use these to deeply understand their identity, strengths, and ambitions:

            - Strengths (what they’re known for): {q1}
            - Interests (what excites them): {q2}
            - Audience (who they want to speak to): {q3}
            - Creator Identity (style and vibe): {q4}
            - Experience or Teachables (what they can share or teach): {q5}

            Your task:
            Recommend the **Top 3 LinkedIn content niches** this person should explore. For each niche:
            1. **Name the niche clearly.**
            2. Explain in **2–3 persuasive sentences** why this niche is a strong match — blend internal fit (interests, strengths) and external opportunity (audience demand, saturation gap).
            3. List **2–3 notable LinkedIn creators or YouTubers** they can study. (If exact names are hard to source, describe the type of creators and how to find them using LinkedIn or SocialBlade.)
            4. Suggest a **starter content series** idea — something they can repeat weekly to build traction (e.g., “Tool Tuesdays,” “Startup Operator Diaries”).
            5. Add **one sentence of advice** on how to differentiate themselves in that niche.

            Reference this additional domain knowledge when needed:
            {context}

            The tone should be encouraging, but clear and strategic — like a mentor helping someone gain direction and focus.
            """
            result = llm.invoke(prompt)
            st.success("🎯 Here are your top 3 niche recommendations:")
            st.markdown(result.content)
