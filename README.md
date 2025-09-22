# 🤖 Industry 4.0 Chatbot with RAG & FAISS  

## 📌 Overview
This project is a **chatbot** designed for Industry 4.0 documentation.  
It uses **Retrieval-Augmented Generation (RAG)** with a **FAISS** vector database and a **local LLM (Ollama)** to answer questions from PDF files.  

The app provides:
- 📂 PDF ingestion and chunking  
- 🧠 Semantic search using FAISS  
- 🤖 LLM-powered answers with context from documents  
- 🧪 Unit tests for core functionalities  
- 🖥 Web interface built with **Streamlit**

---

## ⚙️ Features
- Upload any Industry 4.0 PDF document  
- Retrieve relevant text chunks using FAISS similarity search  
- Generate accurate answers with **Ollama LLM**  
- Unit tests ensure correctness and reliability  

---

## 🛠 Tech Stack
- **Python 3.9+**  
- **LangChain**  
- **FAISS**  
- **HuggingFace Embeddings** (`all-MiniLM-L6-v2`)  
- **Streamlit** (for UI)  
- **Ollama LLM** (`gemma:2b`)  

---

## 📂 Project Structure
industry4.0-chatbot/
│-- data/ # PDF files
│-- chatbot.app # Streamlit UI
│-- chatbot_core.py # Core logic: PDF loading, embeddings, FAISS, RAG
│-- test_chatbot.py # Unit tests
│-- requirements.txt # Dependencies
│-- README.md # Project documentation

yaml
Copy code

---

## 🚀 Installation  

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/industry4.0-chatbot.git
cd industry4.0-chatbot
Create a virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
📄 Usage
Run the Streamlit app:

bash
Copy code
streamlit run chatbot.app
Open your browser at http://localhost:8501.

🧪 Running Tests
Run unit tests with:

bash
Copy code
python -m unittest test_chatbot.py
This will test:

Search function correctness

Empty query handling

Answer relevance and formatting
