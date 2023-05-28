from typing import List

from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document

from config import CONFIGURATION

PERSIST_DIRECTORY = "docsearch"

class SimilarityRepository:
    vectordb: Chroma

    def __init__(self):
        embedding = OpenAIEmbeddings(openai_api_key=CONFIGURATION.open_api_key)
        self.vectordb = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embedding)

    def similarity_search(self, query, limit=4) -> List[Document]:
        return self.vectordb.similarity_search(query, limit=limit)