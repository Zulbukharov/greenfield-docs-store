from typing import List

from fastapi import APIRouter, Depends, status

from schemas.pydantic.similarity import SimilaritySearchResponse, SimilaritySearchRequest

from services.similarity import SimilarityService

SimilarityRouter = APIRouter(prefix="/api/v1", tags=["vectorstore"])

@SimilarityRouter.post("/documents", response_model=List[SimilaritySearchResponse])
def similarity_search_documents(
    request: SimilaritySearchRequest,
    similarityService: SimilarityService = Depends(),
):
    return similarityService.search_documents(request.question)


@SimilarityRouter.post("/commands", response_model=List[SimilaritySearchResponse])
def similarity_search_commands(
    request: SimilaritySearchRequest,
    similarityService: SimilarityService = Depends(),
):
    return similarityService.search_commands(request.question)
