# 🎥 YouTube Script Writer

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-Custom%20or%20MIT-green)

A single-file Streamlit application that generates YouTube video scripts using Google’s Generative AI model through `langchain_google_genai`.

## ✨ Features
- Choose tone, script length, number of key points, and language (English / Hindi Roman / Hinglish)
- AI-generated scripts with:
  - Engaging hook  
  - Structured main points  
  - Stage directions  
  - Closing call-to-action
- Download scripts as text files
- Clean and interactive web UI

## 🧩 Requirements
- Python 3.8+
- streamlit
- langchain_google_genai

Install dependencies:
```
pip install streamlit langchain_google_genai
```

## ⚙️ Setup
1. Open `youtube_script_writer.py`.
2. Add your Google API key to `st.secrets` or environment variables.
3. Check that the model name in `GoogleGenerativeAI` (for example, `"gemini-pro"`) is correct.

## ▶️ Run the App
```
streamlit run youtube_script_writer.py
```

## 💡 Notes
- Do not commit API keys to GitHub or public repos.
- Track usage and costs via your Google Cloud account.
- You can adjust parameters like temperature or word count directly in the script.

## 📄 License
Add a license of your choice (MIT, Apache 2.0, etc.).
```


