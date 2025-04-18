from pydantic import BaseModel, Field
from fastapi import Query
from .sample_enum import SampleEnum


class SampleQuery(BaseModel):
    aa: str = Query(
        ...,
        title="aa title here",
        description="aa description here",
        max_length=50,
        min_length=3,
        example="sample query",
    )
    num_q: int = Query(
        ...,
        title="num_q title here",
        description="num_q description here",
        ge=1,
        le=100,
    )
    nullable_q: int | None = Query(
        10,
        title="nullable_q title here",
        description="nullable_q description here",
    )
    # list treat as body
    list_q: list[str] = Query(
        ...,
        title="list_q title here",
        description="list_q description here",
    )
    enum_q: SampleEnum = Query(
        ...,
        title="Sample enum",
        description="Sample enum for the item to search in items",
    )
