from langchain_google_genai import GoogleGenerativeAI
import streamlit as st
# ----------------------
# Setup
# ----------------------
st.set_page_config(page_title="🎬 YouTube Script Writer", page_icon="🎥", layout="centered")
# Your Google API Key (⚠️ Better to store in st.secrets, but using inline as requested)
GOOGLE_API_KEY = "AIzaSyByCu_b1l5y-aDlphKFpOETS_znDivZTCU"

llm = GoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.8
)
# ----------------------
# UI Layout
# ----------------------
st.title("🎥 YouTube Script Writer")
st.markdown("Write engaging **YouTube video scripts** in your preferred language using AI.")
# Sidebar options
st.sidebar.header("⚙️ Script Settings")
tone = st.sidebar.selectbox("Tone / Style", ["Casual", "Funny", "Motivational", "Professional"])
points = st.sidebar.slider("Number of key points", 3, 7, 4)
length = st.sidebar.radio("Script Length", ["Short (2-3 min)", "Medium (5 min)", "Long (8+ min)"])
language = st.sidebar.selectbox("Script Language", ["Hindi (Roman letters)", "English", "Hinglish"])

# ----------------------
# Bigger Title for Topic Input
# ----------------------
st.markdown("<h3 style='font-size:22px; color:#333;'>🎬 Enter YouTube video topic:</h3>", unsafe_allow_html=True)
topic = st.text_input("", placeholder="e.g. AI se paisa kaise kamaye?")
# ----------------------
# Script Generation
# ----------------------
if st.button("🚀 Generate Script"):
    if topic.strip():
        # Language-specific instructions
        if language == "Hindi (Roman letters)":
            lang_instruction = "Write the script in spoken Hindi, but **type it in Roman letters** (Hindi written in English script)."
        elif language == "English":
            lang_instruction = "Write the script fully in conversational English."
        else:  # Hinglish
            lang_instruction = "Write the script in Hinglish (mix of Hindi and English), typed in Roman letters."

        prompt = f"""
You are a professional YouTube scriptwriter.

Topic: "{topic}"

Tone: {tone}
Script Length: {length}
Number of points to cover: {points}

{lang_instruction}

Include:
- A catchy hook
- Engaging introduction
- {points} clear points with storytelling
- A call to action (Like, Subscribe)
- A natural outro

Add stage directions like (laugh), (pause), (excited tone), etc.
"""
        with st.spinner("🧠 Generating your script..."):
            try:
                response = llm.invoke(prompt)
                st.success("✅ Script Generated!")
                st.markdown("### 📜 Your YouTube Script")
                st.write(response)

                # Download option
                st.download_button("💾 Download Script", response, file_name="youtube_script.txt")

            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
    else:
        st.warning("❌ Please enter a topic first.")
