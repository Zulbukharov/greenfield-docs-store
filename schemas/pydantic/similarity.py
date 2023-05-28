from pydantic import BaseModel


class SimilaritySearchRequest(BaseModel):
    question: str


class SimilaritySearchResponse(BaseModel):
    content: str
    meta: str