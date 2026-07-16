# 📄 AI Text Summarizer Tool

## 📌 Project Overview

The AI Text Summarizer Tool is a Streamlit-based web application that summarizes long articles or documents into concise and meaningful summaries using Google's Gemini API and LangChain.

The application splits large text into smaller chunks using LangChain's RecursiveCharacterTextSplitter, processes each chunk with Gemini AI, and combines the results into a final summary.

---

## 🚀 Features

* 🤖 AI-powered text summarization using Gemini API
* 📄 Supports long articles and documents
* ✂️ LangChain Text Splitter for handling large text
* 📏 Three summary modes:

  * Short
  * Medium
  * Detailed
* 📊 Word Count
* 🔠 Character Count
* 📥 Download Summary as TXT
* ⚡ User-friendly Streamlit interface

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* LangChain
* Python Dotenv

---

## 📦 Installation

Clone the repository:
🌐 Live Demo
```bash
https://aleenashah965-hue-text-summarizer-tool-app-jcobwa.streamlit.app/

Clone the repository:
```bash
https://github.com/Aleenashah965-hue/Text_Summarizer_Tool.git

Install the required libraries:

```bash
pip install -r requirements.txt
```

```env
GOOGLE_API_KEY=API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## 📷 How to Use

1. Launch the application.
2. Paste a long article or document.
3. Select the AI model.
4. Choose the summary length (Short, Medium, or Detailed).
5. Click **Generate Summary**.
6. View the generated summary.
7. Download the summary as a text file if needed.

---

## 📁 Project Structure

```
Text_Summarizer_Tool/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🎯 Purpose

This project demonstrates how to use Generative AI and LangChain to summarize long text efficiently. It helps users save time by extracting the most important information from lengthy documents.

---

## 👩‍💻 Developed By

**Aleena Shah**

BS Computer Science

UET Mardan

AlgoHub Generative AI Internship – Week 3
