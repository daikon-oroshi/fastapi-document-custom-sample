from pydantic import BaseModel, Field
from .sample_enum import SampleEnum


class SampleQuery(BaseModel):
    """
    SampleQuery docstring here
    """

    aa: str = Field(
        ...,
        title="aa title here",
        description="aa description here",
        max_length=50,
        min_length=3,
        example="sample query",
    )
    num_q: int = Field(
        ...,
        title="num_q title here",
        description="num_q description here",
        ge=1,
        le=100,
    )
    nullable_q: int | None = Field(
        10,
        title="nullable_q title here",
        description="nullable_q description here",
    )
    nullable_default_none: int | None = Field(
        None,
        title="nullable_default_none title here",
        description="nullable_default_none description here",
    )
    list_q: list[str] = Field(
        ...,
        title="list_q title here",
        description="list_q description here",
    )
    enum_q: SampleEnum = Field(
        ...,
        title="Sample enum",
        description="Sample enum for the item to search in items",
    )
