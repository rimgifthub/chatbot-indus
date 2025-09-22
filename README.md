# Industry 4.0 Lab Chatbot 

A intelligent chatbot application that answers questions about Industry 4.0 concepts using document-based knowledge retrieval and local language models.

##  Overview

This chatbot leverages advanced NLP techniques including document embedding, vector similarity search, and local language models to provide accurate answers about Industry 4.0 topics. The application features a user-friendly Streamlit interface and supports PDF document uploads for custom knowledge bases.

##  Features

- **Document-Based Q&A**: Upload PDF documents and ask questions about their content
- **Smart Retrieval**: Uses FAISS vector database for efficient similarity search
- **Local LLM**: Powered by Ollama's Gemma 2B model for privacy and offline operation
- **Web Interface**: Clean Streamlit UI for easy interaction
- **File Upload**: Support for custom PDF document uploads
- **Pre-trained Embeddings**: Uses HuggingFace's all-MiniLM-L6-v2 model for document embeddings

##  Technology Stack

- **Frontend**: Streamlit
- **Document Processing**: LangChain, PyPDFLoader
- **Embeddings**: HuggingFace Transformers (all-MiniLM-L6-v2)
- **Vector Database**: FAISS
- **Language Model**: Ollama (Gemma 2B)
- **Text Processing**: RecursiveCharacterTextSplitter

##  Project Structure

```
├── chatbot_app.py          # Main Streamlit application
├── chatbot_core.py         # Core chatbot functionality and database setup
├── test.py                 # Unit tests for chatbot functions
├── requirements .txt       # Project dependencies
└── README.md              # Project documentation
```

##  Installation

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- Gemma 2B model downloaded in Ollama

### Setup Steps

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd industry-4-0-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r "requirements .txt"
   ```

3. **Install and setup Ollama**
   ```bash
   # Install Ollama from https://ollama.ai/
   ollama pull gemma:2b
   ```

4. **Prepare your PDF document**
   - Place your Industry 4.0 PDF document as `industry-4-0.pdf` in the project root
   - Or use the file upload feature in the web interface

##  Usage

### Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run chatbot_app.py
   ```

2. **Access the web interface**
   - Open your browser to `http://localhost:8501`

3. **Interact with the chatbot**
   - Upload a PDF document (optional - defaults to `industry-4-0.pdf`)
   - Ask questions about Industry 4.0 concepts
   - Get AI-powered answers based on the document content

### Example Questions

- "What is Industry 4.0?"
- "What are the key components of Industry 4.0?"
- "How does IoT relate to Industry 4.0?"
- "What are the benefits of smart manufacturing?"

### Running Tests

```bash
python test.py
```

##  Configuration

### Model Settings

The chatbot uses the following default configurations:

- **LLM Model**: Gemma 2B via Ollama
- **Temperature**: 0 (deterministic responses)
- **Max Tokens**: 150
- **Retrieval**: Top 3 most similar document chunks
- **Chunk Size**: 1000 characters with 100 character overlap

### Customization

You can modify these settings in `chatbot_core.py`:

```python
# Adjust chunk size and overlap
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=100
)

# Change LLM parameters
llm = Ollama(
    model="gemma:2b", 
    temperature=0, 
    num_predict=150
)

# Modify retrieval parameters
retriever = db.as_retriever(search_kwargs={"k": 3})
```

##  Testing

The project includes comprehensive unit tests covering:

- **Search Functionality**: Tests exact match and empty query handling
- **Answer Generation**: Validates keyword relevance and response formatting
- **Database Operations**: Ensures proper document loading and indexing

Run tests with detailed output:
```bash
python test.py -v
```

##  Key Dependencies

- `streamlit`: Web application framework
- `langchain-community`: Document loaders and vector stores
- `langchain-core`: Core LangChain functionality
- `sentence-transformers`: Text embeddings via HuggingFace
- `faiss-cpu`: Efficient similarity search
- `PyPDF2/pypdf`: PDF document processing

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Troubleshooting

### Common Issues

1. **Ollama Connection Error**
   - Ensure Ollama is running: `ollama serve`
   - Verify Gemma model is installed: `ollama list`

2. **PDF Loading Issues**
   - Check file path and permissions
   - Ensure PDF is not password-protected

3. **Memory Issues**
   - Reduce chunk size or number of retrieved documents
   - Use smaller embedding models

### Performance Tips

- Use SSD storage for faster vector database operations
- Increase retrieval parameter `k` for more comprehensive answers
- Adjust chunk size based on your document structure

##  Future Enhancements

- Support for multiple document formats (DOCX, TXT, etc.)
- Multi-language support
- Advanced conversation memory
- Integration with cloud-based LLMs
- Real-time document indexing
- Enhanced UI with chat history

---

**Built with for Industry 4.0 education and research**
