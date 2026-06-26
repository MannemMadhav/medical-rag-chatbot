from typing import List

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Medical question from the user",
    )


class ChatResponse(BaseModel):
    answer: str
    sources: List[str]