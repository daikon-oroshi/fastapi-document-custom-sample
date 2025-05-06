from fastapi import APIRouter, Query, Path
from typing import Annotated
from fastapi.responses import PlainTextResponse
from schema import SampleQuery, SampleRequest, SampleResponse
from tags import SAMPLE_TAG, SAMPLE_TAG2


router1 = APIRouter(prefix="/sample", tags=[SAMPLE_TAG.name])


GET_SAMPLE_DESCRIPTION = """
## Sample description here
- aaa
- bbb
- ccc

### subtitle 3
* aaa description here
* aaa description here
"""


@router1.get(
    "/",
    summary="get_sample sammary here \n",
    description=GET_SAMPLE_DESCRIPTION,
    operation_id="getSample",
    response_class=PlainTextResponse,
    response_description="response description here",
)
async def get_sample(query: Annotated[SampleQuery, Query()]):
    print(query)
    return ""


router2 = APIRouter(prefix="/sample2", tags=[SAMPLE_TAG2.name])


ItemId = Annotated[
    int,
    Path(
        ...,
        title="item_id title here",
        description="item_id description here",
        ge=1,
        le=100,
        example=10,
    ),
]


@router2.post(
    "/{item_id}/{item_id2}",
    summary="create_item summary here",
    description="create_item description here",
    response_model=SampleResponse,
    status_code=201,
)
async def create_item(
    request: SampleRequest,
    item_id: ItemId,
    item_id2: int = Path(
        ...,
        title="item_id title here",
        description="item_id description here",
        ge=1,
        le=100,
        example=10,
    ),
):
    print(request)
    print(item_id)
    print(item_id2)
    return SampleResponse(
        res_str="aa",
        res_sub_model={"a": 1, "b": True},
        res_list=["aa"],
        res_list2=["cc", "dd"],
    )
