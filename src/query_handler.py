import google.generativeai as genai
from src.vector_store import load_vector_store
from src.prompt_template import create_prompt_template

def handle_user_query(user_question, index_name="faiss_index"):
    """
    Searches for relevant text in the vector store and generates a response using Gemini.
    """
    vector_store = load_vector_store(index_name)
    docs = vector_store.similarity_search(user_question)

    # Combine relevant document contents
    context = "\n\n".join([doc.page_content for doc in docs])

    # Format the prompt
    prompt = create_prompt_template()
    formatted_prompt = prompt.format(context=context, question=user_question)

    # Generate response using Gemini AI
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(formatted_prompt)

    return response.text if response.text else "No response generated."
