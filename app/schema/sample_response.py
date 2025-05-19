from typing import Annotated, List
from annotated_types import Len
from pydantic import BaseModel, Field
from .sample_enum import PrefCode


AlNum = Annotated[
    str,
    Field(
        ...,
        title="AlNum title here",
        description="AlNum description here",
        example="aaaa",
        pattern=r"^[a-zA-Z0-9]+$",
    ),
]

AlNumList = Annotated[
    List[AlNum],
    Len(max_length=2),
    Field(
        ...,
        title="AlNumList title here",
        description="AlNumList description here",
        example=["aaaa", "bbbb"],
        min_length=2,
    ),
]


class ResponseSubModel(BaseModel):
    a: int = Field(...)
    b: bool = Field(...)


SubModelFeild = Annotated[
    ResponseSubModel,
    Field(
        ...,
        title="SubModelFeild title here",
        description="SubModelFeild description here",
        example=ResponseSubModel(a=1, b=True),
    ),
]


class SampleResponse(BaseModel):
    """
    SampleResponse docstring here
    """

    res_str: AlNum = Field(..., description="req_str description here")

    res_sub_model: SubModelFeild = Field(...)

    res_list: AlNumList
    res_list2: AlNumList = Field(
        ...,
        title="req_list2 title here",
        description="req_list2 description here",
        example=["vvv", "ddd"],
    )
    pref_code: PrefCode

    # nullable_q: int | None = Annotated[]
