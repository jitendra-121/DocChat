from langchain.prompts import PromptTemplate

def create_prompt_template():
    """
    Creates a structured prompt for querying the Gemini model.
    """
    prompt_template = """
    Answer the question as detailed as possible from the provided context. 
    If the answer contains structured data like tables or lists, respond in the same format. 
    If the answer is not in the provided context, say, "The answer is not available in the context."

    Context:
    {context}

    Question:
    {question}
    """

    return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])
