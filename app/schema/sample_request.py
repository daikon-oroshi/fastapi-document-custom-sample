from pydantic import Field, BaseModel
from .sample_query import SampleQuery


class ReqSubModel(BaseModel):
    """
    SubModel docstring here
    """

    sub_str: str = Field(
        ...,
        title="sub_str title here",
        description="sub_str description here",
        max_length=50,
        min_length=3,
    )
    sub_int: int = Field(
        ...,
        title="sub_int title here",
        description="sub_int description here",
        ge=1,
        le=100,
    )


class SampleRequest(SampleQuery):
    """
    SampleRequest docstring here
    """

    req_sub_model: ReqSubModel = Field(
        ...,
        title="req_sub_model title here",
        description="req_sub_model description here",
    )
