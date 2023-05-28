from typing import List

from fastapi import Depends

from repository.similarity import SimilarityRepository
from schemas.pydantic.similarity import SimilaritySearchResponse


class SimilarityService:
    similarityRepository: SimilarityRepository

    def __init__(self, similarityRepository: SimilarityRepository = Depends()) -> None:
        self.similarityRepository = similarityRepository

    def search(self, query, limit=4) -> List[SimilaritySearchResponse]:
        return [SimilaritySearchResponse(content=record.page_content, meta=record.metadata['source']) for record in  self.similarityRepository.similarity_search(query, limit=limit)]