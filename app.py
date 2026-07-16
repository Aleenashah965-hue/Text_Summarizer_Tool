from google import genai
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st
import os

# Load API Key
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found.")
    st.stop()

# Gemini Client
client = genai.Client(api_key=api_key)

# Page Settings
st.set_page_config(
    page_title="📄 Text Summarizer Tool",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 AI Text Summarizer Tool")

# Welcome Message
st.success("""
Welcome!

Paste any long article or document and generate an AI-powered summary using Gemini and LangChain.
""")

# Sidebar
st.sidebar.title("⚙️ Settings")

model = st.sidebar.selectbox(
    "Select AI Model",
    [
        "gemini-2.5-flash",
        "gemini-2.5-pro"
    ]
)

summary_length = st.sidebar.selectbox(
    "Summary Length",
    [
        "Short",
        "Medium",
        "Detailed"
    ]
)

# User Input
text = st.text_area(
    "📄 Paste your article here",
    height=300
)

# Generate Button
generate = st.button("📝 Generate Summary")

if generate:

    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")

    else:

        # Summary Instructions
        if summary_length == "Short":
            instruction = "Summarize the text in 3 to 5 bullet points."

        elif summary_length == "Medium":
            instruction = "Summarize the text in one detailed paragraph."

        else:
            instruction = "Provide a detailed summary with headings and bullet points."

        # LangChain Text Splitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_text(text)

        final_summary = ""

        # Generate Summary for each Chunk
        for chunk in chunks:

            prompt = f"""
{instruction}

Text:

{chunk}
"""

            try:

                with st.spinner("⏳ Generating Summary..."):

                    response = client.models.generate_content(
                        model=model,
                        contents=prompt
                    )

                    final_summary += response.text + "\n\n"

            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.stop()

        # Display Summary
        st.subheader("📄 AI Summary")
        st.write(final_summary)

        # Success Message
        st.success("✅ Summary Generated Successfully!")

        # Word Count
        st.info(f"📝 Word Count: {len(final_summary.split())}")

        # Character Count
        st.info(f"🔠 Character Count: {len(final_summary)}")

        # Download Button
        st.download_button(
            label="📥 Download Summary",
            data=final_summary,
            file_name="summary.txt",
            mime="text/plain"
        )

# Footer
st.markdown("---")
st.caption("Developed by Aleena Shah | Text Summarizer Tool | Week 3 Project")