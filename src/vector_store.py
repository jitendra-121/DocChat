from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load Hugging Face embeddings model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_and_save_vector_store(text_chunks, index_name="faiss_index"):
    """
    Creates a FAISS vector store and saves it locally.
    """
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local(index_name)

def load_vector_store(index_name="faiss_index"):
    """
    Loads the FAISS vector store.
    """
    return FAISS.load_local(index_name, embeddings, allow_dangerous_deserialization=True)
