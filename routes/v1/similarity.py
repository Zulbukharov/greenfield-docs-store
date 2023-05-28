from typing import List

from fastapi import APIRouter, Depends, status

from schemas.pydantic.similarity import SimilaritySearchResponse, SimilaritySearchRequest

from services.similarity import SimilarityService

SimilarityRouter = APIRouter(prefix="/api/v1", tags=["vectorstore"])

@SimilarityRouter.post("/similarity", response_model=List[SimilaritySearchResponse])
def similarity_search(
    request: SimilaritySearchRequest,
    similarityService: SimilarityService = Depends(),
):
    return similarityService.search(request.question)
