import streamlit as st
import warnings

# Ignorar advertencias de FutureWarning de transformers
from transformers import tokenization_utils_base
warnings.filterwarnings("ignore", category=FutureWarning, module='transformers.tokenization_utils_base')

from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.schema.runnable import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

# 1. Vectorize the bug history csv data
loader = CSVLoader(file_path="sample-problem-solution.csv")
documents = loader.load()
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(documents, embeddings)

# 2. Function for similarity search
def retrieve_info(query):
    similar_bugs = db.similarity_search(query, k=3)
    bug_info_array = [doc.page_content for doc in similar_bugs]
    return bug_info_array

# 3. Setup prompts and chain
llm = Ollama(model="phi")  # This uses Phi-2 model

template = """
You are a helpful senior developer assisting junior developers with their coding issues.
I will share a junior developer's question with you, and you will provide the best answer
based on past bug reports and solutions. Please follow ALL of the rules below:

1/ Your response should be clear, concise, and easy for a junior developer to understand.
2/ Use the provided bug history to inform your answer, but feel free to elaborate or provide additional context if necessary.
3/ If the bug history doesn't contain a direct solution, use it as a starting point to suggest troubleshooting steps or potential solutions.
4/ Always encourage good coding practices and suggest resources for further learning when appropriate.

Below is the question from the junior developer:
{question}

Here is relevant information from our bug history database:
{bug_history}

Please provide the best response to help this junior developer:
"""

prompt = PromptTemplate(
    input_variables=["question", "bug_history"],
    template=template
)

chain = (
    {"question": RunnablePassthrough(), "bug_history": lambda x: retrieve_info(x["question"])}
    | prompt
    | llm
)

# 4. Generate response
def generate_response(question):
    return chain.invoke({"question": question})

# 5. Build an app with streamlit
def main():
    st.set_page_config(
        page_title="Bug History Search Assistant", page_icon=":bug:")
    st.header("Bug History Search Assistant :bug:")
    
    question = st.text_area("What's your coding question?")
    
    if st.button("Submit"):
        if question:
            with st.spinner("Searching bug history and generating response..."):
                try:
                    result = generate_response(question)
                    st.success("Response generated successfully!")
                    st.info(result)
                    
                    # Add debug information
                    st.write("Debug Information:")
                    st.write(f"Question: {question}")
                    st.write(f"Response type: {type(result)}")
                    st.write(f"Response length: {len(str(result))}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a question.")

if __name__ == '__main__':
    main()
