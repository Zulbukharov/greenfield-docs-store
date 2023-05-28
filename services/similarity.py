from typing import List

from fastapi import Depends

from repository.similarity import CommandStoreRepository, DocumentStoreRepository
from schemas.pydantic.similarity import SimilaritySearchResponse


class SimilarityService:
    docSearchRepository: DocumentStoreRepository

    def __init__(self, docSearchRepository: DocumentStoreRepository = Depends(), commandSearchRepository: CommandStoreRepository = Depends()) -> None:
        self.docSearchRepository = docSearchRepository
        self.commandSearchRepository = commandSearchRepository

    def search_documents(self, query, limit=4) -> List[SimilaritySearchResponse]:
        return [SimilaritySearchResponse(content=record.page_content, meta=record.metadata['source'] if 'metadata' in record else "") for record in  self.docSearchRepository.similarity_search(query, limit=limit)]
    
    def search_commands(self, query, limit=4) -> List[SimilaritySearchResponse]:
        return [SimilaritySearchResponse(content=record.page_content, meta=record.metadata['source'] if 'metadata' in record else "") for record in  self.docSearchRepository.similarity_search(query, limit=limit)]