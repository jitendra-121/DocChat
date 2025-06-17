import streamlit as st
from src.pdf_processing import extract_pdf_text, split_text_into_chunks
from src.vector_store import create_and_save_vector_store
from src.query_handler import handle_user_query

# Initialize session state for chat history
def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def main():
    """
    Main function to run the Streamlit app.
    """
    initialize_session_state()
    
    st.set_page_config("Chat PDF")
    st.header("Chat with your Document")
    
    # Display previous chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input for user questions
    if prompt := st.chat_input("Ask a question about your document"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = handle_user_query(prompt)
                    st.write(response)
                    
                    # Save assistant's response
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error generating response: {str(e)}")

    # Sidebar for PDF Upload
    with st.sidebar:
        st.title("Upload PDF 📂")
        st.write("*This is for demonstration purposes. Do not submit any proprietary documents.*")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

        if st.button("Process"):
            if not pdf_docs:
                st.error("Upload a PDF to start!")
                return

            with st.spinner("Processing, Chunking, and Caching..."):
                raw_text = extract_pdf_text(pdf_docs)
                text_chunks = split_text_into_chunks(raw_text)
                create_and_save_vector_store(text_chunks)
                st.success("Processing Done ✅")

if __name__ == "__main__":
    main()
