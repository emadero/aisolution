# aisolution
AI Solution for RAG from CSV Using Ollama, Chroma, and Hugging Face

# Bug History Search Assistant

This project is an AI-powered bug history search assistant that leverages Retrieval Augmented Generation (RAG) to retrieve relevant bug reports from a CSV file and generate helpful answers for developers. It uses Ollama, FAISS, and Hugging Face embeddings to process the data, with an interface built using Streamlit.

## Features

- Load and vectorize bug history data from a CSV file.
- Perform similarity search on the bug reports using FAISS and Hugging Face embeddings.
- Use Ollama's LLM for language generation and deliver concise answers.
- Interactive Streamlit web interface to submit coding questions and retrieve solutions based on historical bugs.

## Requirements

- Python 3.8+
- Pipenv (for environment and dependency management)

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/bug-history-search-assistant.git
   cd bug-history-search-assistant
   ```

2. Install dependencies using Pipenv:

   ```bash
   pipenv install
   ```

3. Activate the Pipenv environment:

   ```bash
   pipenv shell
   ```

4. Environment Variables: Ensure you have a `.env` file in the project root with the necessary environment variables:

   ```bash
   touch .env
   ```

   Add the following variables to the `.env` file:

   ```ini
   # .env file
   CSV_FILE_PATH=path_to_your_csv_file/sample-problem-solution.csv
   ```

5. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## How to Use

1. **Upload the CSV file**: Ensure the bug history CSV file is located in the project directory or specified in the `.env` file.
2. **Run the app**: Use Streamlit to run the application. You will be able to input questions into the text area and receive responses generated from past bug reports.
3. **Submit your question**: After entering your coding-related question, click on the "Submit" button to generate a response.
4. **View the results**: The app will display a response, debug information, and links to relevant past bug reports.

## Code Overview

- **Data Vectorization**: The bug history CSV is loaded and converted into embeddings using Hugging Face's all-MiniLM-L6-v2 model. The FAISS vector store is used to store and retrieve similar bug reports based on your query.
- **Retrieval Process**: When a user submits a question, the app performs a similarity search on the vectorized bug reports and retrieves the most relevant ones.
- **Language Generation**: Ollama's LLM (Language Model) is used to generate a coherent and helpful response based on the retrieved bug history and the user's question.

## Dependencies

- Streamlit: Web app framework for building the interface.
- FAISS: Vector similarity search library for fast retrieval.
- Hugging Face: Provides embeddings for text vectorization.
- Ollama: Used for language generation in answering queries.
- Pipenv: For managing dependencies and virtual environments.

## Acknowledgments

Special thanks to the open-source libraries and tools that made this project possible, including Langchain, FAISS, Hugging Face, and Streamlit.

Feel free to modify or extend the project according to your needs.
