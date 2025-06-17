# DocuChat AI

DocuChat AI is a RAG-powered application that allows users to upload PDF documents and interact with them using natural language queries. The app extracts text from PDFs, processes it into embeddings, and enables users to ask questions about the content using AI-powered responses.

[[Huggingface Spaces Demo]](https://huggingface.co/spaces/tejacherukuri/DocuChat)

## Features

-  **Upload PDFs**: Supports multiple PDF file uploads.
-  **Text Extraction**: Extracts text from uploaded PDFs.
-  **Chunking & Embeddings**: Processes text into meaningful chunks and stores them in a vector database.
-  **AI-Powered Chat**: Ask questions and get intelligent responses based on document content.
-  **Efficient Processing**: Uses FAISS for fast similarity search and retrieval.

## File Structure

```plaintext
DocuChat/
│── app.py                    # Main Streamlit application
│── src/                      # Source code directory
│   │── config.py             # configures Gemini
│   │── pdf_processing.py     # Handles PDF text extraction and chunking
│   │── prompt_template.py    # Handles prompt engineering and invokes llm
│   │── query_handler.py      # Handles user queries and responses
│   │── vector_store.py       # Manages FAISS vector database
│── requirements.txt          # Required dependencies
│── README.md                 # Documentation
```

## Technologies Used

- **Python**
- **Streamlit** for UI
- **PyPDF2** for text extraction
- **FAISS** for vector search
- **HuggingFace Embeddings** for text representations
- **Google Gemini API** for AI-powered responses

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/tejacherukuri/DocuChat.git
   cd DocuChat
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set up your Gemini API key:
   ```
   export GEMINI_API_KEY="your_api_key"
   ```
2. Run the application:
   ```
   streamlit run app.py
   ```
3. Upload a PDF and start chatting with your document!

## Notes

⚠️ *This application is for demonstration purposes. Do not submit proprietary or confidential documents.*

## Future Enhancements

- Support for additional document formats (e.g., Word, TXT).
- Enhanced summarization features.
- Improved AI response accuracy with fine-tuned models.

