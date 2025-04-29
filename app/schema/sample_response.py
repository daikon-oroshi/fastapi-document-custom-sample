from pydantic import BaseModel, Field


class SampleResponse(BaseModel):
    """
    SampleResponse docstring here
    """

    nullable_q: int | None = Field(
        10,
        title="Page size",
        description="Number of items to be returned per page",
        ge=1,
    )
