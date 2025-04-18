from pydantic import BaseModel, Field


class BRequest(BaseModel):
    """
    aaaaaaa
    """

    b: str = Field(
        ...,
        title="Request string",
        description="Request string for the item to search in items",
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
    nullable_q: int | None = Field(
        10,
        title="Page size",
        description="Number of items to be returned per page",
        ge=1,
    )
