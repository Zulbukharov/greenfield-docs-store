import yaml
from pydantic import BaseModel, Field


class Struct(BaseModel):
    open_api_key: str = Field(..., min_length=1)
    # s3_endpoint: str = Field(..., min_length=1)
    # s3_access_key: str = Field(..., min_length=1)
    # s3_secret_key: str = Field(..., min_length=1)
    # s3_region: str = Field(..., min_length=1)

    # redis_url: str = Field(..., min_length=1)

    # pdf_loader: str = Field(..., min_length=1)
    # text_splitter: str = Field(..., min_length=1)
    # chunk_size: int = Field(...)

    # chroma_server_host: str = Field(..., min_length=1)
    # chroma_server_port: str = Field(..., min_length=1)

    # # condense_question_prompt: str = Field(..., min_length=1)
    # doc_qa_prompt: str = Field(..., min_length=1)
    # summarize_prompt: str = Field(..., min_length=1)
    # law_consult_prompt: str = Field(..., min_length=1)
    # lang_prompt: str = Field(..., min_length=1)

    class Config:
        validate_assignment = True


with open("config.yml") as stream:
    try:
        CONFIGURATION = Struct.parse_obj(yaml.safe_load(stream))
    except Exception as e:
        print(e)
        exit(1)
