# Launching the Application

This is a backend application built using `FastAPI` framework. It contains two routers for handling WebSockets and HTTP requests respectively.

Before launching the application, you will need to set the `OPEN_API_KEY` environment variable, as it is required for the application to run.

## To launch the application, follow these steps:

- Clone the repository to your `local machine`.
- Install the required dependencies by running `pip install -r requirements.txt`.
- Set the `OPEN_API_KEY` environment variable with your API key.
- Run the application using the command `uvicorn main:app --reload`.
- The application should now be running on `http://localhost:8000/`.

## Overview

1. Конструктор для различных пакетов для работы с [PDF](https://python.langchain.com/en/latest/modules/indexes/document_loaders.html)
2. Конструктор для выбора определенного [разделителя текста](https://python.langchain.com/en/latest/modules/indexes/text_splitters.html) (Char, Recursive, NLTK, Tiktoken)
   Необходимо учитывать параметры (chunk_size, chunk_overlap)
3. Конструктор для выбора [vector storage](https://python.langchain.com/en/latest/modules/indexes/vectorstores.html) (chroma, pinecone)
   Необходимо принимать параметры для запуска по определенному типу
   Необходимо принимать [embedder](https://python.langchain.com/en/latest/modules/models/text_embedding.html) (OpenAIEmbeddings)
4. Создать кастомный chain

# Pipeline
