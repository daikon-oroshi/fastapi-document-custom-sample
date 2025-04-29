from pydantic import BaseModel, Field


class SampleRequest(BaseModel):
    """
    SampleRequest docstring here
    """

    b: str = Field(
        ...,
        title="b title here",
        description="b description here",
        max_length=50,
        min_length=3,
    )
    b_num: int = Field(
        ...,
        title="Page number",
        description="Page number of the results to be returned",
        ge=1,
        le=100,
    )
    pageno: int | None = Field(
        10,
        title="Page size",
        description="Number of items to be returned per page",
        ge=1,
    )
    perpage: int | None = Field()
